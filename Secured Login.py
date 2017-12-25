# Miguel Bigueur
# Secured Login
# Security Scripting w/Python
# 12/24/2017

import paramiko
ssh = paramiko.SSHClient()
ssh.connect('127.0.0.1', username='jesse', password='lol')
