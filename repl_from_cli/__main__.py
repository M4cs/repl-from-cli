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
def main():
    signal.signal(signal.SIGINT, lambda x, y: sys.exit(1))
    config = GithubConfigCheck()
    gh = Github(config.token)
    user = gh.get_user()
    SOURCE_DIR = os.path.realpath('.')
    name_of_repo = input('What Would You Like To Name This Repo?: ')
    print('Creating Repo...', end='\r')
    repo = None
    try:
        repo_create = user.create_repo(name_of_repo)
    except Exception as e:
        raise Exception(e)
    if repo_create:
        print('Repo Creation Complete!')
    else:
        print('Something went wrong... Exiting...')
        exit(1)
    os.chdir(SOURCE_DIR)
    os.system('git init')
    os.system('git add .')
    os.system('git commit -m "Adding Files from repl-from-cli"')
    if config.uses_ssh_keys:
        os.system('git remote add origin git@github.com:{}'.format(repo_create.full_name))
    else:
        os.system('git remote add origin https://github.com/{}'.format(repo_create.full_name))
    os.system('git push -u origin master')
    print('Checking Repo Is Ready For Cloning To repl.it...')
    res = requests.get('https://api.github.com/repos/{}/{}'.format(user.login, name_of_repo))
    obj = json.loads(res.content)
    if obj.get('message') == "Not Found":
        print('Couldn\'t find the repository on GitHub... Try Again.')
        exit(1)
    else:
        print('Repo Is Ready!')
    delete = ask_yes_no('Would you like to delete the repo from your GitHub page?')
    print('Starting repl.it Clone...')
    open_new_tab('https://repl.it/github/{}/{}'.format(user.login, name_of_repo))
    if delete:
        print('Waiting 10 Seconds Until Repository Deletion...')
        count = 0
        while count <= 10:
            print('Time Until Deletion: ' + str(count) + ' sec.', end='\r')
            count += 1
            time.sleep(1)
        print('Deleting Repository...')
        repo = gh.get_repo(repo_create.full_name)
        repo.delete()
        shutil.rmtree('.git')
        print('Deletion Complete. Your source is now on your repl.it account!')
    print('Repl.it Upload Complete!')

if __name__ == "__main__":
    main()
