'''
#11)python program to accept a hyphen separated sequence of words as input and
#print the words in a Hyphen-separated sequence after sorting them alphabetically
#eg:hello-good-morning-to-all
#expected o/p:all-good-hello-morning-to

x=input("enter a hyphen seperated sequence of words : ")
x=x.split("-")
print(x)
y=sorted(x)
y="-".join(y)
print(y)
#"-".join(sorted(x.split("-")))


#####write a python program to print the number of characters in a given string
#frequency of characters

x=input("enter a string : ")
chars=sorted(x)
#print(chars)
d1={}
for i in set(chars):
    #print(i,":",chars.count(i))
    d1[i]=chars.count(i)
print(d1)

   
####python program to count the occurances of each word in a given string

x=input("enter a string : ")
words=x.split()
d1={}
for i in set(words):
    d1[i]=words.count(i)
print(d1)



#python program to check substring is present ina given string

x=input("enter a string : ")
y=input("enter a substring to find : ")
if y in x:
    print("substring is present in main string",x)
else:
    print("substring not found in main string",x)



#write a python program to get a string made of the first 2 and the last 2 chars
#from a given string.if the string length is less than 2, return instead of
#the empty string

#sample string : "tecnosoft"
#expected result:"teft"
#sample string:"w3"
#expected result:"w3w3"
#sample string:"w"
#expected result:empty string

x=input("enter a string : ")
if len(x)>=2:
    print(x[:2]+x[-2:])
    
else:
    print("empty string")



#write a python program to get a string from a given string where all occurances
#of its first char have been changed to except the first char itself
#eg: enter string:restart
#expected o/p:resta$t

x=input("enter a string : ")
x=x[0]+x[1:].replace(x[0],"$")
print(x)



#write a python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string
#sample string: 'abc','xyz'
#expected result:'xyc abz"

x=input("enter a string 1 : ")
y=input("enter a string 2 : ")
#z=y[:2]+x[-1]+" "+x[:2]+y[-1]##
z=y[:-1]+x[-1]+" "+x[:-1]+y[-1]
print(z)


#write a python program to add "ing" at the end of a given string
#(length should be atleast 3).if the given string already ends witn "ing"
#then add "ly" instead.
#if the string length of the given string is less than 3, leave it unchanged
#sample string:"abc"
#expected result:"abcing"
#sample string:"string"
#expected string:"stringly"

x=input("enter a string : ")
if len(x)>=3:
    if x[-3:]!="ing":
        print(x+"ing")
    else:
        print(x+"ly")
else:
    print(x)
    
'''
#write a python program to take a list of words separated by comma
#returns the length of the longest one

#sample string:hello,good,morning,to,everyone
#expected result:"everyone"

#sample string:"warm, wishes, to, python, devops,class
#expected o/p: "wishes"

x=input("enter a list of strings : ")
a=[]


























    
    












    








