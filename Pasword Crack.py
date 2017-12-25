# Written by Miguel Bigueur
# Password Crack
# Security Scripting w/Python
# Dec 24, 2017

import string
import hashlib
import sys

hfd = open('hashes.txt', 'r') # open the file with hashes
afd = open('answers.txt', 'w') # open the file to write answers to

for hash in hfd.readlines():
    wordlist = open('/Users/miguelbigueur/Library/Mobile Documents/com~apple~CloudDocs/PyCharm Files/untitled/OPSC 540/Week 4/password.lst')
    for word in wordlist.readlines():
        hash = string.strip(hash)
        pswd = string.strip(word)
        '''hashes the password using md5 then compares to hash in rainbow table'''
        if hashlib.md5(pswd).hexdigest() == hash:
            print (pswd)
            '''writes the "standard output" to the answers.txt document'''
            sys.stdout = afd

    wordlist.close()
afd.close()
