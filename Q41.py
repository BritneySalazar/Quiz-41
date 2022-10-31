Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
string = "H# m# n@#e i# Br#t#3y."
hastag = '#'

def count_hastag(string, hastag):
    total = 0
    index = 0
    while index < len(string):
        if string[index: index + 1] == hastag:
            total += 1
            index += 1
        else:
            index += 1
    return total

count_hastag(string, hastag)
6

#Britney S CPSC Q41