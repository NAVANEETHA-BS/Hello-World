#1) write a python function to find the Max of three numbers

'''

def num():
    x=int(input("enter a number 1 : "))
    y=int(input("enter a number 2 : "))
    z=int(input("enter a number 3 : "))
    n=max(x,y,z)
    print("max number among three numbers is : ",n)
    

num()

---------------------------------

def num(x,y,z):
    c=max(x,y,z)
    return c

m=num(10,30,15)
print(m)

-----------------------------------------------------------------

#2)write a python function to sum all the numbers in a list
#sample list : (8,2,3,0,7)
#expected o/p : 20

def num():
    x=(8,2,3,0,7)
    n=sum(x)
    print("sum of all the numbers in a list : ",n)

num()

-------------------------------------------

def num(a,b,c,d,e):
    m=(a,b,c,d,e)
    n=sum(m)
    return n

m=num(8,2,3,0,7)
print(m)

----------------------------------------

def total(a):
    global sum1
    sum1=sum1+a

sum1=0

for i in range(1,6):
    x=int(input("enter a number : "))
    total(x)
print("Total=",sum1)

---------------------------------------

def total(a):
    sum=0
    for i in a:
        sum=sum+i
    return sum

x=[8,2,3,0,7]
k=total(x)
print("Total of", x,"is : ",k)

----------------------------------------------------------------------

#3)write a python program to multiply all the numbers in a list
#sample list : (8,2,3,-1,7)
#expected o/p: -336

def mul():
    mul=1
    x=[8,2,3,-1,7]
    for i in x:
        mul=mul*i
    print(mul)

mul()
        

-----------------------------------------
def multi(a):
    mul=1
    for i in a:
        mul=mul*i
    return mul
    

for i in range(1,6):
    x=int(input("enter a number : "))
    z=multi(x)
print("multiplication of is : ",z)
  
---------------------------------------    
def total(a):
    mul=1
    for i in a:
        mul=mul*i
    return mul

x=[8,2,3,-1,7]
k=total(x)
print("Total of", x,"is : ",k)

---------------------------------------

def total(a):
    global mul
    mul=mul*a

mul=1

for i in range(1,6):
    x=int(input("enter a number : "))
    total(x)
print("Total=",mul)

----------------------------------------------------------------------------------

#4) write a python program to reverse a string
#sample string: "1234abcd"
#Expected Output: "dcba4321"

def rev(a):
    a=a[::-1]
    return a

    
x=input("enter a string : ")
b=rev(x)
print("Reversed string : ",b)

--------------------------------------------

def rev():
    a=input("enter a string : ")
    x=a[::-1]


rev()
print(x)

---------------------------------------------------------------------

#5)write a python program to calculate the factorial of a given number


def num(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact

x=int(input("enter a number : "))    
k=num(x)
print(k)
      
---------------------------------------

def num():
    n=int(input("enter a number : "))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
        
num()

-------------------------------------------------------------------------


#6)write a python function to check whether a number is in a given range

def num():
    x=int(input("enter a number : "))
    for i in range(1,11): 
        if x==i:
            print(x," is in a given range")
            break
    else:
        print(x,"is not in a given range")
        

num()

------------------------------------------


def num(a):
    for i in range(1,11):
        if a==i:
            
            return True
    else:
        
        return False 



x=int(input("enter a number : "))
k=num(x)
if k:
    print(k," is in a given range")
else:
    print(k," is not in a given range")

-------------------------------------------------------------------------------

#7)write a python function that accepts a string and calculate the numbers of
#upper case letters and lower case letter
#sample string: 'The quick Brow Fox'
#Expected Output:
#No. of upper case characters:3
#No. of Lower case Characters:12


def cnt():
    global count1,count2
    if i.isupper():
        count1+=1
        print("number of uppercase letters : ",count1)   
    else:
        count2+=1
        print("number of lowercase letters : ",count2)

            

x=input("enter a string : ")
count1=0
count2=0
for i in x:
    cnt()    

---------------------------------------------


def cnt(a,b):
    global count1,count2
    if i.isupper():
        a+=1
        print("number of uppercase letters : ",a)   
    else:
        b+=1
        print("number of lowercase letters : ",b)
    return a,b

            

x=input("enter a string : ")
count1=0
count2=0
for i in x:
    z=cnt(count1,count2)
    print(z[0],z[1])

--------------------------------------------

#8)write a python function that takes a list and returns a new list
#with unique elements of the first list
#sample list: [1,2,3,3,3,3,4,5]
#unique list: [1,2,3,4,5]

x=[1,2,3,3,3,3,4,5]
y=[]
for i in x:
    y.append(i)

print(set(y))

--------------------


def uniq(a):
    y=[]
    for i in a:
        y.append(i)
    return y
    



x=[1,2,3,3,3,3,4,5]
k=uniq(x)
print(set(k))
   
---------------------


def uniq():
    y=[]
    for i in x:
        y.append(i)
    print(set(y))


x=[1,2,3,3,3,3,4,5]
uniq()

---------------------------------------------------

#9)write a python function that takes a number as a parameter and check
#the number is prime or not
#note: A prime number(or a prime) is a natural number greater than 1 and
# that has no positive divisors other than 1 and itself.


def prime(a):   
    for i in range(2,x):
        
        if x%i==0:
            #return False
            print(x,"is  not a prime number")
            break
    else:
        #return True
        print(x,"is   a prime number")
    

    

x=int(input("enter a number : "))
if x>1:
    prime(x)
    #k=prime(x)
    #if k:
        #print(x,"is  not a prime number")
    #else:
        #print(x,"is a prime number")


--------------------------------------------

def prime(a):   
    for i in range(2,x):
        
        if x%i==0:
            return True
            
            break
    else:
        return False
        
    

    

x=int(input("enter a number : "))
if x>1:
    
    k=prime(x)
    if k:
        print(x,"is  not a prime number")
    else:
        print(x,"is a prime number")


--------------------------------------------------------------------

#10)write a python program to print the even numbers from a given list
#sample list: [1,2,3,4,5,6,7,8,9]
#Expected result: [2,4,6,8]



x=[1,2,3,4,5,6,7,8,9]
y=[]
for i in x:
    if i%2==0:
        y.append(i)
    print(y)
        
--------------------

def even(a):
    y=[]
    for i in a:
        if i%2==0:
            y.append(i)
    print(y)
    

x=[1,2,3,4,5,6,7,8,9]
even(x)

-----------------


def even(a):

    if a%2==0:
        y.append(a)
    return y
    #print(y)

            
    

x=[1,2,3,4,5,6,7,8,9]
y=[]
for i in x:
    k=even(i)
print(k)

-----------------------------------------------------------------------------


#11)write a python function that checks whether a passed string is palindrome or not
# Note: A palindrome is a word,phrase, or sequence that reads the same backward as forward,
# example:madam or nurses run


def pali():
    if x==x[::-1]:
        print(x,"is a palindrome")
    else:
        print(x,"is not a palindrome")
    
    


x=input("enter a string : ")
pali()

------------------------------------


def pali(a):
    if x==x[::-1]:
        return True
    else:
        return False





x=input("enter a string : ")
k=pali(x)
if k:
    print(x,"is a palindrome")
else:
    print(x,"is not a palindrome")

----------------------------------------------------------------------


#12)write a python function to chect whether a string is a pangram or not
#Note: Pangrams are words or sentences containing every letter of the alphabet atleast once
#for example: "The quick brown fox jumps over the lazy dog"


import re
x=input("enter a string : ")
x=x.lower()
alphas=re.findall("[a-z]",x)

d1={}
for i in alphas:
    cnt=alphas.count(i)
    d1[i]=cnt

if len(d1)==26:
    print("it is a panagram string")
else:
    print("it is not a panagram string")


----------------------------------------------------------


#13)write a python program that accepts a hyphen-separated sequence of words
#as input and prints the words in a hyphen separated sequence after
#sorting them alphabetically
#sample items:green-red-yellow-black-white
#expected result:black-green-red-white-yellow

x=input("enter a hythen separated string : ")
x=x.split("-")
x=sorted(x)
y="-".join(x)
print(y)

-------------------------------


def hyphen():
    x=input("enter a hythen separated string : ")
    x=x.split("-")
    x=sorted(x)
    y="-".join(x)
    print(y)
    


hyphen()
----------------------------------------------------


#14)write a python function to create and print a list where the values are
#square of numbers between 1 and 30(both included)

def sqr():
    x=[i*i for i in list(range(1,31))]
    print(x)


sqr()

-----------------------------

x=[i*i for i in list(range(1,31))]
print(x)

'''






































































































