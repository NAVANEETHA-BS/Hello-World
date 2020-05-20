#python program to detect both strings are anagrams
'''
x=input("enter a string1 : ")
y=input("enter a string2 : ")
x=sorted(x)
y=sorted(y)
print(x)
print(y)
if sorted(x)==sorted(y):
    print("both strings are anagrams")
else:
    print("both strings are nagrams")
 '''

#python program to find number of words and number of chars

'''
x=input("enter a string : ")
chars=len(x)
print(chars)
words=len(x.split(" "))
print(words)
'''

#python program to count number of lowercase characters in a string
'''
x=input("enter a string : ")
lcnt=0
for i in x:
    if i.islower():
        lcnt+=1
print(lcnt)
'''

#python program to check string palindrome or not
'''
x=input("enter a string : ")
if x==x[::-1]:
    print(x,"is a palindrome")
else:
    print(x,"is not a palindrome")

'''

#python program to accept hyphen separated sequence of words as input and
# print hyphen separated sequence of words alphabetically
'''
x=input("enter a hyphen separated sequence of words : ")
x=x.split("-")
x=sorted(x)
x="-".join(x)
print(x)
'''

#python program to count the occurances of each word in a given string
'''
x=input("enter a string : ")
x=x.split()
d1={}
for i in set(x):
   d1[i]=x.count(i)
print(d1)
'''

#python program to check substring is present in a given string
'''
x=input("enter a string : ")
y=input("enter a substring : ")
if y in x:
    print("substring is present in given string")
else:
    print("substring is not present in given string")
'''

#python program to get a string made of first two and last two chars from
#given string, if string length is less than two return empty string
'''
x=input("enter a string : ")
if len(x)>=2:
    x=x[:2]+x[-2:]
    print(x)
else:
    print("empty string")
'''

#write a python program to get a string where all occurances of its
#first  char have been changed to except the first char itself
'''
x=input("enter a string :")
x=x[0]+x[1:].replace(x[0],'#')
print(x)
'''




































    












































