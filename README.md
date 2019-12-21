# repl-from-cli
A new way to get your source code onto Repl with one command.

![Stars](https://img.shields.io/github/stars/M4cs/repl-from-cli) ![Forks](	https://img.shields.io/github/forks/M4cs/repl-from-cli) [![Downloads](https://pepy.tech/badge/repl-from-cli)](https://pepy.tech/project/repl-from-cli) ![Tweet](	https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2FM4cs%2Frepl-from-cli)

<p align="center">
  <a href="repl.art" target="_blank">
  <img src="http://repl.art/ghrepl.png" width="200px">
  <img src="http://repl.art/octocat-replbot1.png" width="200px">
  <img src="http://repl.art/octocat-replbot2.png" width="200px">
  </a>
  <br>
  <p align="center">Art From repl.art</p>
</p>

# What is repl-from-cli?

Repl-from-cli allows you to upload your source code to a temporary GitHub repository and then allows you to clone it to repl.it and either delete or save the repo on your GitHub. You basically get to hit 2 birds with 1 stone.

# How does it work?

This tool uses the GitHub API through PyGithub and the `git` command line tool. It uses a Python program to create and pull repositories on GitHub to your local directory, push to remote, pull to repl.it, and then either delete the repo, or save it! You'll need a few things to get started.

Requirements:

- Python 3.5+
- A GitHub Account
- A GitHub Personal Access Token ([How Do I Get Mine?](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)) **Make sure to give it Repo, User, and Delete Permissions**
- A [repl.it](https://repl.it) Account

# Getting Started

To start, first make sure you have `git` the command line tool installed. If you are using GitHub you most likely have it installed but if you don't [find out how here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). 

Either Run:
```
pip3 install repl-from-cli
```

or

```
# After pulling this repo and going into the directory:
python3 setup.py install
```

To install the `repl-from-cli` command.

The tool pulls from `~/.replitcli/config` for configuration values. To change your GitHub token remove the `config` file there. This will run the startup wizard again and allow you setup your config.

# Usage

Run `repl-from-cli` inside any directory you'd like to upload to repl.it. It will make sure you are logged into repl before creating the repository. After it creates the repo on your github it will create a local git repo in the directory and push to the GitHub repo. If you want to hide files you should make a `.gitignore` prior to running this command. Also if it already has a GitHub repo it simply uses the URL API repl.it provides (ex. `https://repl.it/github/<Username>/<Repo Name>`).

The tool will open up `repl.it` in your default browser. **Make sure you are logged into repl.it on it.**


# License

Modified Copyright License. I hereby declare that anybody is allowed to pull, fork, and modify this code locally for personal use or contribution to the main branch. You may not UNDER ANY CIRCUMSTANCES redistribute this code as your own apart from Forking. 

Copyright Max Bridgland 2019
