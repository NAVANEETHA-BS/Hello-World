# check alphabet or not
'''
0-9 =>48-57
A-Z =>65-90

ord() :it return given character ascii value
eg:  ord('A') =>65

chr() :it return given ascii value character
eg: chr(65) => A

'''

ch=input("enter a character: ")
if len(ch)==1:
    #if ch.lower() in "abcdefghijklmnopqrstuvwxyz":
    if (ord(ch))>=65 and (ord(ch))<=90 or (ord(ch))>=97 and (ord(ch))<=122:
        print("given character is alphabet")
    else:
        print("given character is not an alphabet")
else:
    print("plz enter only one character")
