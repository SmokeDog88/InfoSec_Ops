# Written by Miguel Bigueur
# Port Scan
# Security Scripting w/Python
# Dec 24, 2017

import os
import argparse
import sys
import subprocess
import platform

parser = argparse.ArgumentParser(description='Search for specific UIDs in passwd file')
parser.add_argument(dest='filenames', metavar='filename', nargs='*')
parser.add_argument('-i', '--input', metavar='', dest='shell_input', required=False)
parser.add_argument('-u', '--user', required=True, dest='usernames', action='append', help='Usernames to search for')
parser.add_argument('-o', '--outfile', metavar='', dest='outfile', action='store', help='output file')

group = parser.add_mutually_exclusive_group()
group.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
group.add_argument('--speed', dest='speed', action='store', choices={'slow', 'fast'}, default='slow',
                   help='search speed')
args = parser.parse_args()

user = args.usernames

print('Your operating system is: ', sys.platform)
print('Your platform release is: ', platform.release())
print('Your platform version is: ', platform.version())
print('Your current working directory is: ', os.getcwd())


if __name__ == '__main__':
    for name in args.usernames:
        if sys.platform == 'darwin' or 'linux' or 'freebsd':
            print('You entered username: ', name)
            with open('/etc/passwd', "r")as f:
                for line in f:
                    if line.split(":")[0] == name:
                        with open(args.outfile, 'a') as f1:
                            f1.write(line)
    print('Your output file has been updated! ')

shell_input = args.shell_input

try:
    shell_command = ' '.join(['ls', '-l', shell_input])
    '''Here, the program runs long listing on the file revealing user permissions and group/file memberships.'''

    print('shell command: ' + shell_command)

    shell_output = subprocess.check_output(shell_command) # when adding shell=True, shell injection becomes possible.
    '''Here we execute the sanitized input without shell=True.
       When shell=True is used, shell injection is possible as proved by trying both methods.'''

    print(shell_output) # print the input argumante's command to screen
except subprocess.CalledProcessError:
    print('Ooops, Something went awry!')
except FileNotFoundError:
    print('No such file or directory ', shell_input)
