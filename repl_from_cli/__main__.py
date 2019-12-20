from repl_from_cli.core.git.helper import GithubConfigCheck
from repl_from_cli.core.helpers import ask_yes_no
from github import Github
from webbrowser import open_new_tab
from git import Repo
import requests
import signal
import sys
import time
import shutil
import json
import os

CURR_DIR = os.getcwd()


def create_repository(user, repo_name, source_dir, uses_ssh_keys):
    """ Given the user, repo_name, source_dir, and uses_ssh_keys, create a github repo, repo_name, from source_dir,
     using ssh or not, as required. """
    print('Creating Repo...', end='\r')
    try:
        repo_create = user.create_repo(repo_name)
    except Exception as e:
        raise Exception(e)
    if repo_create:
        print('Repo Creation Complete!')
    else:
        print('Something went wrong... Exiting...')
        exit(1)
    os.chdir(source_dir)
    os.system('git init')
    os.system('git add .')
    os.system('git commit -m "Adding Files from repl-from-cli"')
    if uses_ssh_keys:
        os.system('git remote add origin git@github.com:{}'.format(repo_create.full_name))
    else:
        os.system('git remote add origin https://github.com/{}'.format(repo_create.full_name))
    os.system('git push -u origin master')
    print('Checking Repo Is Ready For Cloning To repl.it...')
    res = requests.get('https://api.github.com/repos/{}/{}'.format(user.login, repo_name))
    obj = json.loads(res.content)

    if obj.get('message') == "Not Found":
        return False, repo_create
    else:
        return True, repo_create


def parse_args():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("repo_name", nargs="?", default=None)
    parser.add_argument("--preserve_repo", default=None)
    parser.add_argument("--source_dir", default=os.path.realpath('.'))
    args = parser.parse_args()
    if args.repo_name is None:
        args.repo_name = name_of_repo = input('What Would You Like To Name This Repo?: ')
    if args.preserve_repo is None:
        args.preserve_repo = ask_yes_no('Would you like to delete the repo from your GitHub page?')
    else:
        while True:
            if args.preserve_repo.lower() == 'y':
                args.preserve_repo = True
            elif args.preserve_repo.lower() == 'n':
                args.preserve_repo = False
            else:
                print('Please Choose Y or N')
                args.preserve_repo = input(
                    str('Would you like to delete the repo from your GitHub page?' + ' [Y\\N]: '))
    return args.repo_name, args.preserve_repo, args.source_dir


def delete_repo(gh, repo_create):
    print('Waiting 10 Seconds Until Repository Deletion...')
    count = 0
    while count <= 10:
        print('Time Until Deletion: ' + str(10 - count) + ' sec.', end='\r')
        count += 1
        time.sleep(1)
    print('Deleting Repository...')
    repo = gh.get_repo(repo_create.full_name)
    repo.delete()
    shutil.rmtree('.git')
    print('Deletion Complete. Your source is now on your repl.it account!')


def main():
    signal.signal(signal.SIGINT, lambda x, y: sys.exit(1))
    config = GithubConfigCheck()
    gh = Github(config.token)
    user = gh.get_user()

    repo_name, preserve_repo, source_dir = parse_args()
    sucessful, repo_create = create_repository(user, repo_name, source_dir, config.uses_ssh_keys)

    if not sucessful:
        print('Couldn\'t find the repository on GitHub... Try Again.')
        exit(1)
        
    print('Repo Is Ready!')
    print('Starting repl.it Clone...')
    open_new_tab('https://repl.it/github/{}/{}'.format(user.login, repo_name))

    if not preserve_repo:
        delete_repo(gh, repo_create)

    print('Repl.it Upload Complete!')


if __name__ == "__main__":
    main()
