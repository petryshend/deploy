#!/usr/bin/python
import subprocess
import sys

from parameters import USER, HOST, PASSWORD

sudo = 'echo -e "%s" | sudo -S ' % PASSWORD

COMMANDS = [
    sudo + 'apt-get install -y curl',
    sudo + 'apt-get install -y git',
    sudo + 'apt-get install -y apache2',
    sudo + 'add-apt-repository -y ppa:ondrej/php5-5.6',
    sudo + 'apt-get update',
    sudo + 'apt-get install -y python-software-properties',
    sudo + 'apt-get update',
    sudo + 'apt-get install -y php5',
    sudo + 'apt-get install -y php5-pgsql',
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
