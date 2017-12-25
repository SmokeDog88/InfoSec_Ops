# Written by Miguel Bigueur
# Password Strength Checker
# Security Scripting w/Python
# Dec 24, 2017

import string
import re

afd = open('answers.txt', 'r')

la = r'[a-z]' # Regular expression to check for any capital letters in the specified range
ua = r'[A-Z]' # Regular expression to check for any lower case letters in the specified range
n = r'[0-9]'  # Regular expression to check for any numbers in the specified range
sc = r'[!@#$%^&*]' # Regular expression to check for any special characters in the specified range

for word in afd.readlines():
    pswd = string.strip(word)
    good_len =  False
    lower = False
    upper = False
    num = False
    special = False
    score = 0
    if len(pswd) > 6: # Check to ensure minimum number of characters is greater than 6
        good_len = True
        score += 1
    if re.search(la, pswd): # lowercase alpha search
        lower = True
        score += 1
    if re.search(ua, pswd): # upper alpha search
        upper = True
        score += 1
    if re.search(n, pswd):   # numbers search
        num = True
        score += 1
    if re.search(sc, pswd): # special characters
        special = True
        score += 1
    print("results for %s: score: %d" % (pswd,score))
    print("good_len: %s, lower: %s, upper: %s, num: %s, special: %s" % (good_len, lower, upper, num, special))
