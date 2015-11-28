#!/usr/bin/python
import subprocess
import sys

from parameters import USER, HOST, PASSWORD

sudo = 'echo -e "Pi171717" | sudo -S '

COMMANDS = [
    sudo + 'apt-get install -y curl',
    sudo + 'apt-get install -y git',
    sudo + 'apt-get install -y apache2',
    sudo + 'apt-get install -y php5',
    sudo + 'curl -sS https://getcomposer.org/installer | php',
    sudo + 'mv composer.phar /usr/local/bin/composer',
    sudo + 'chown -R %s:%s /var/www' % (USER, USER),
]

commands_string = ' && '.join(COMMANDS)

ssh = subprocess.Popen(["ssh", "%s" % HOST, commands_string],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)


result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print ''.join(result)
