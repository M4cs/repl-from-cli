from repl_from_cli.core.helpers import ask_yes_no
from getpass import getpass
from webbrowser import open_new_tab
from base64 import b64encode, b64decode
import os, json, time


CONFIG_PATH = os.path.realpath(os.path.expanduser('~') + '/.replitcli')

class GithubConfigCheck:
    def __init__(self):
        has_config = False
        if os.path.exists(CONFIG_PATH):
            if os.path.exists(os.path.realpath(CONFIG_PATH + '/config')):
                has_config = True
        else:
            os.makedirs(CONFIG_PATH)
        if not has_config:
            print('Please Generate A Personal Access Token\nURL: https://github.com/settings/tokens')
            gh_token = getpass('Token: ')
            uses_ssh_keys = ask_yes_no('Do you use ssh keys to authenticate?')
            config_obj = {
                'GH_TOKEN': gh_token,
                'USES_SSH_KEYS': uses_ssh_keys
            }
            base_64_bytes = b64encode(json.dumps(config_obj).encode())
            print('Please Make Sure You Are Logged Into https://repl.it in Your Default Browser')
            time.sleep(2)
            open_new_tab('https://repl.it')
            input('Press ENTER to Continue')
            with open(CONFIG_PATH + '/config', 'wb') as f:
                f.write(base_64_bytes)
        config = None
        with open(CONFIG_PATH + '/config', 'rb') as f:
            rb = f.read().decode('utf-8')
            config = json.loads(b64decode(str(rb)))
        self.token = config['GH_TOKEN']
        self.uses_ssh_keys = config['USES_SSH_KEYS']

