# Security Scripting w/Python
# Miguel Bigueur
# Assignment Part 1

from urllib.request import urlopen
from bs4 import BeautifulSoup

# first: acquire full html content from web page
html = urlopen("https://www.champlain.edu/current-students")

# then read and parse html code and save into a variable
bsObj = BeautifulSoup(html.read(), "html.parser")

# use tag and id to isolate specific targeted data
link = bsObj.findAll("div", {"id":"audience-nav"})

'''iterate through lines containing li looking for a tags. 
iterate once more through output for a tags and print out line
with a tags, this also creates newline due to the looping iteration'''
for li in link:
    output = li.findAll("a")
    for a in output:
        print(a)
