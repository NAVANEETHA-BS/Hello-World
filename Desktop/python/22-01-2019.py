'''
#python program to detect if two strings are anagrams
#ex:anagram,nagaram,both are anagram strings
#ex:hello,world,both are nagaram strings 


x=input("enter a string1 : ")
y=input("enter a string2 : ")

if sorted(x)==sorted(y):
    print("both are anagram strings ")
else:
    print("both are nagaram strings")



#python program to calculate number of words and number of characters present in
#a given string
#ex: hello good morning to all
#expected output: 

x=input("enter a string : ")
chars=len(x)
words=len(x.split(" "))
print("no of chars: ",chars)
print("no of words: ",words)



#python program to count number of lowercase characters in a string

x=input("enter a string : ")
lcnt=0
for i in x:
    if i.islower():
        lcnt+=1
print("No of lowercase letters in a",x,"is",lcnt)

#python program to check string palindrome or not
x=input("enter a string : ")
if x==x[::-1]:
    print("string is palindrome  ")
else:
    print("string is not a palindrome ")
'''


#11)python program to accept a hyphen separated sequence of words as input and print the words in a Hyphen-separated 
#sequence after sorting them alphabetically
#eg:hello-good-morning-to-all
#expected o/p:all-good-hello-morning-to

x=input("enter a hyphen seperated sequence of words : ")













    
