import subprocess
import os


work = '''Host github.com
 HostName github.com
 IdentityFile ~/.ssh/wonderkey'''


os.system('echo "{}" >> ~/.ssh/config')

os.system("eval 'ssh-agent -s'")