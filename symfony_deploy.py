#!/usr/bin/python
import subprocess
import sys

from parameters import USER, HOST, APP_FOLDER

PASSWORD = raw_input('Enter server\'s sudo password')

sudo = 'echo -e "%s" | sudo -S ' % PASSWORD

COMMANDS = [
    'cd %s' % APP_FOLDER,
    'git reset --hard',
    'git pull --rebase',
    'composer install',
    sudo + 'chmod -R 777 app/cache app/logs',
    'php app/console cache:clear --env=prod',
    sudo + 'chmod -R 777 app/cache app/logs',
    'php app/console doctrine:schema:update --force',
    'git reset --hard'
]

commands_string = ' && '.join(COMMANDS)

ssh = subprocess.Popen(["ssh", "%s@%s" % (USER, HOST), commands_string],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)


result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print ''.join(result)


