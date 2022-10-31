Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

 
string = ()
hashtag = "#"

def hash_spam(string, hashtag):
    index = 0
    total = 0
    while index < len(string):
        if string[index: index + 1] == hashtag:
            total += 1
            index += 1
        else:
            index += 1
    if total >= 4:
        print("This tweet will be considered as a spam!")
    else:
        return total

    
hash_spam(string, hashtag)
0

hash_spam("########", hashtag)
This tweet will be considered as a spam!

#Britney Salazar Quiz 42 CPSC