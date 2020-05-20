
'''
name1 = "rama"
name2 = "janu"
name1list = list(name1)
name2list = list(name2)
for i in name1list:
    if i in name2list:
        idx = name1list.index(i)
        name1list[idx] = "_"
        idx = name2list.index(i)
        name2list[idx] = "_"
print(name1list)
print(name2list)

names = name1list + name2list

cnt=0
for i in names:
    if(i!="_" and i!=" "):
        cnt+=1
print(cnt)


f = list('flames')
index = 0
while len(f)>1:
    for i in range(cnt):
        index+=1
        if index>len(f):
            index = 1
    f.remove(f[index-1])
    index-=1
print(f)

------------------------------------------------------------------------
num=[' ','one','two','three','four','five','six','seven','eight','nine','ten'\
     'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen',\
     'eighteen','nineteen']
two_digit=[' ',' ','twenty','thirty','forty','fifty','sixty','seventy',\
           'eighty','ninety']
x = int(input("enter a number : "))
output = " "
if (x==0):
    output="zero"
elif (x<=19):
    output = num[x]
elif (x<=99):
    output = two_digit[x//10]+" "+num[x%10]
print(output)
--------------------------------------------------------------------------


name1 = 'ram'
name2 = 'janu'
name1list = list(name1.upper())
name2list = list(name2.upper())
for i in name1list:
    if i in name2list:
        idx = name1list.index(i)
        name1list[idx] = '-'
        idx = name2list.index(i)
        name2list[idx] = '-'
print(name1list)
print(name2list)

names = name1list + name2list
cnt=0
for l in names:
    if (l!="-" and l!=" "):
        cnt+=1
print(cnt)

f=list('flames')
index=0
while(len(f)>1):
    for i in range(cnt):
        index+=1
        if index>len(f):
            index=1
    f.remove(f[index-1])
    index-=1
print(f)
---------------------------------------------------------------

num=[' ','one','two','three','four','five','six','seven','eight','nine',\
     'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',\
     'seventeen','eighteen','nineteen']
two_digit=[' ',' ','twenty','thirty','fourty','fifty','sixty','seventy',\
           'eighty','ninety']
x=int(input("enter a number : "))
total = " "
if (x=='0'):
    total='zero'
elif(x<=19):
    total=num[x]
elif(x<=99):
    total=two_digit[x//10]+" "+num[x%10]
print(total)
---------------------------------------------------------------

name1 = 'ram'
name2 = 'janu'
name1list = list(name1)
name2list = list(name2)
for i in name1list:
    if i in name2list:
        idx = name1list.index(i)
        name1list[idx]="_"
        idx = name2list.index(i)
        name2list[idx] = "_"
print(name1list)
print(name2list)

names = name1list+name2list
cnt=0
for l in names:
    if(l!="_" and l!=" "):
        cnt+=1
print(cnt)

f=list('flames')
index=0
while(len(f)>1):
    for i in range(cnt):
        index+=1
        if index>len(f):
            index=1
    f.remove(f[index-1])
    index-=1
print(f)
---------------------------------------------------------

num=[' ','one','two','three','four','five','six','seven','eight',\
     'nine','ten','eleven','twelve','thirteen','fourteen','fifteen',\
     'sixteen','seventeen','eighteen','nineteen']
two_digit=[' ',' ','twenty','thirty','fourty','fifty',\
           'sixty','seventy','eighty','ninety']
total=" "
x=int(input("enter a number : "))
if(x==0):
    total='zero'
elif(x<=19):
    total=num[x]
elif(x<=99):
    total=two_digit[x//10]+" "+num[x%10]
print(total)
-------------------------------------------

num=int(input("enter a number : "))
row=0
while row<num:
    space=num-row-1
    while space>0:
        print(end=" ")
        space=space-1
    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    row=row+1
    print()

-------------------------------------------------------

  *
 ***
*****


x=int(input("enter a number : "))
row=0
for i in range(1,x+1,2):
    print((x-(row+1))*" ",i*"*")
    row=row+1


------------------------------------------------------

    *
   * *
  * * *
 * * * *
* * * * *

x=int(input("enter a number : "))
for i in range(1,x+1):
    print((x-i)*" ",i*"* ")
---------------------------------------------

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

n=int(input("enter a number : "))

for i in (range(1,n+1)):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#print()
---------------------------------------------------

*
**
***
****
*****

n=int(input("enter number of rows : "))
for i in range(1,n+1):
    print(i*"*")

-------------------------------------------------

1
22
333
4444
55555

n=int(input("enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        i=str(i)
    print(i*j)
-----------------------------------------------------

n=int(input("enter number of rows :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        i=str(i)
    print(j*i)
        
-------------------------------------------------------


n = int(input("enter number of rows : "))
row=0
for i in range(1,n+1):
    print(1*"*"+" "*(i-1)+(1)*"*")
-----------------------------------------------------

n=int(input("enter number of rows : "))
for i in range(n,0,-1):
    print(j*"*"+(i-j)*" ")
-------------------------------------------------------


n=int(input("enter number of rows : "))
for i in range(n):
    print(" "*(n-i-1),end='')
--------------------------------------------------------

winning_number=43
guess=1
number=int(input("enter number between 1 and 100 : "))
game_over=False

while not game_over:
    if number==winning_number:
        print(f"you win and played {guess} number of times")
        game_over=True
    else:
        if number<winning_number:
            print("too low")
            guess+=1
            number=int(input("enter again: "))
        else:
            print("too high")
            guess+=1
            number=int(input("enter again :"))
                       
-----------------------------------------------------------

winning_number=43
guess=1
number=int(input("enter number between 1 and 100 : "))
game_over=False
while not game_over:
    if number==winning_number:
        print(f"you won, you played {guess}  number of times")
        game_over=True
    else:
        if number<winning_number:
            print("too low")
            guess+=1
            number=int(input("enter again :"))
        else:
            print("too high")
            guess+=1
            number=int(input("enter again :"))
----------------------------------------------------------------


name1='ram'
name2='janu'
name1list=list(name1)
name2list=list(name2)
for l in name1list:
    if l in name2list:
        idx=name1list.index(l)
        name1list[idx]='-'
        idx=name2list.index(l)
        name2list[idx]='-'
print(name1list)
print(name2list)

names=name1list+name2list
cnt=0
for i in names:
    if(i!='-' and i!=' '):
        cnt+=1
print(cnt)

f=list('flames')
index=0
while len(f)>1:
    for k in range(cnt):
        index+=1
        if index>len(f):
            index=1
            f.remove(f[index-1])
            index-=1
print(f)
--------------------------------------------------------------

number=[' ','one','two','three','four','five','six','seven','eight',\
        'nine','ten','eleven','twelve','thirteen','fourteen','fifteen',\
        'sixteen','seventeen','eighteen','nineteen']
two_digit=[' ',' ' ,'twenty','thirty','fourty','fifty','sixty','seventy',\
           'eighty','ninety']
n=int(input("enter number between 1 and 100 : "))
total=''
if n=='zero':
    total=0
elif n<=19:
    total=number[n]
else:
    total=two_digit[n//10]+" "+number[n%10]
print(total)
------------------------------------------------------------------

winning_number=56
guess=1
number=int(input("enter number between 1 and 100 : "))
game_over=False
while not game_over:
    if number==winning_number:
        print(f"you won, and you played {guess} number of times")
        game_over=True
    else:
        if number<winning_number:
            print("too low")
            guess+=1
            number=int(input("enter number again :"))
        else:
            print("too high")
            guess+=1
            number=int(input("enter number again :"))
-----------------------------------------------------------

num=[' ','one','two','three','four','five','six','seven','eight','nine',\
     'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',\
     'seventeen','eighteen','nineteen']
two_digit=[' ',' ','twenty','thirty','fourty','fifty','sixty','seventy',\
           'eighty','ninety']
n=int(input("enter any number :"))
total=" "
if n==0:
    total='zero'
elif n<=19:
    total=num[n]
else:
    total=two_digit[n//10]+" "+num[n%10]
print(total)
--------------------------------------------------------------

name1='ram'
name2='janu'
name1list=list(name1)
name2list=list(name2)
for l in name1list:
    if l in name2list:
        idx=name1list.index(l)
        name1list[idx]='_'
        idx=name2list.index(l)
        name2list[idx]='_'
print(name1list)
print(name2list)

names=name1list+name2list
cnt=0
for l in names:
    if (l!='_' and l!=" "):
        cnt+=1
print(cnt)

f=list('flames')
index=0
while len(f)>1:
    for i in range(cnt):
        index+=1
        if index>len(f):
            index=1
            f.remove(f[index-1])
            index-=1
print(f)
--------------------------------------------------------------------

for row in range(7):
    for col in range(5):
        if (col==0 or col==4) and row!=0 or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()

------------------------------------------------------------------

for row in range(7):
    for col in range(5):
        if(col==0 or col==4 ) or ((row==0 or row==3 or row==6)\
                                  and(col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
----------------------------------------------------------------

for row in range(7):
    for col in range(5):
        if (col==0) or (row==0 or row==6) and (col>0):
            print("*",end="")
        else:
            print(end=" ")
    print()
--------------------------------------------------------------

for row in range(7):
    for col in range(5):
        if (col==0 or col==4) or (row==0 or row==6) and (row>=0 and row<=6):
            print("*",end="")
        else:
            print(end=" ")
    print()
        
-------------------------------------------------------------

for row in range(7):
    for col in range(5):
        if col==0 or (row==0 or row==3 or row==6) and (row>=0 and row<=6):
            print("*",end="")
        else:
            print(end=" ")
    print()

----------------------------------------------------------

for row in range(7):
    for col in range(5):
        if col==0 or (row==0 or row==3) and (col>=0 and col<6):
            print("*",end="")
        else:
            print(end=" ")
    print()

----------------------------------------------------------------
G

for row in range(7):
    for col in range(5):
        if (col==0)or (col==4 and(row>=3 and row<=6)) or (row==0 or row==6) and (col>=0 and col<=6):
            print("*",end="")
        else:
            print(end=" ")
    print()

--------------------------------------------------------------------
H

for row in range(7):
    for col in range(5):
        if row==3 or (col==0 or col==4) and (row>0 and row<6):
            print("*",end="")
        else:
            print(end=" ")
    print()
-------------------------------------------------------------------
I

for row in range(7):
    for col in range(5):
        if (row==0 or row==6) or col==2 and (row>=0 and row<=6):
            print("*",end="")
        else:
            print(end=" ")
    print()
--------------------------------------------------------------
J

for row in range(7):
    for col in range(5):
        if row ==0 and (col>=0 and col<=4) or row==6 and (col>=0 and col<3)\
        or col==2 and (row>0 and row<6):
            print("*",end="")
        else:
            print(end=" ")
    print()
-------------------------------------------------------------
K

i=0
j=4
for row in range(7):
    for col in range(5):
        if (col==0 or (row==col+2 and col>1)) :
            print("*",end="")
        elif ((row==i and col==j) and col>0):
            print("*",end="")
            i=i+1
            j=j-1
        else:
            print(end=" ")
    print()

------------------------------------------------------------------
L

for row in range(7):
    for col in range(5):
        if row==6 or col==0 and (col>=0 and col<=6):
            print("*",end="")
        else:
            print(end=" ")
    print()
-------------------------------------------------------------------

def test_testing_floats(module_name='this module'):
    number1=1.25
    number2=1
    number3=-1
    number4=5/4
    number6=6
    assert(rounding_floats(number1,number2)==1.2)
    assert(rounding_floats(number1*10,number3)==10)
    assert(float_to_fractions(number1)==number4)
    assert(get_denominator(number2,number6)==number6)
    assert(get_numerator(number2,number6)==number2)
    
    s='Tests in {name} have {con}!'.format(name=module_name,con='passed')
    #print(s.format(name=module_name,con='passed'))
    return s

if __name__=='__main__()':
    x=test_testing_floats(module_name='this module')
    print(x)
------------------------------------------------

def convert_to_decimal(number,base):
    multiplier,result=1,0
    while number>0:
        result+=number%10*multiplier
        multiplier*=base
        number=number//10
        return result
------------
def test_convert_to_decimal():
    number,base=1001,2
    assert(convert_to_decimal(number,base)==9)
    print("test passed")
----------------------------
if __name__=='__main__()':
    number,base=1001,2
    assert(convert_to_decimal(number,base)==9)
print("test passed")
    
    #test_convert_to_decimal()

 ----------------------------------------------------------

def finding_gcd(a,b):
    while(b!=0):
        result=b
        a,b=b,a%b
    return result

number1=21
number2=12
#x=assert(finding_gcd(number1,number2)==3)
#print('test passed')
x=finding_gcd(number1,number2)
print(x)
------------------------------------------


import time
import numpy

def trad_version():
    t1=time.time()
    X=range(10000000)
    Y=range(10000000)
    Z=[]
    for i in range(len(X)):
        Z.append(X[i]+Y[i])
    return time.time()-t1

def numpy_version():
    t1=time.time()
    X=numpy.arange(10000000)
    Y=numpy.arange(10000000)
    Z=X+Y
    return time.time()-t1

#if __name__=='__main__()':
print(trad_version())
print(numpy_version())
-----------------------------------

#converting string to list and list to string
x=input("enter a string : ")
x=x.split()
#print(x)
x=x[::-1]
y=" ".join(x)
print(y)
print(type(y))

------------------------------------------
#reverse a string character by character

x=input("enter a string : ")
x=x[::-1]
print(x)
------------------------------------

x=input("enter a string : ")
r=reversed(x)
y="".join(r)
print(y)
-------------------------------------

s='neetha'
output=' '
i=len(s)-1
while i>=0:
    output=output+s[i]
    i=i-1
print(output)
---------------------------------
#reverse internal content of each word

s='My Name Is Navaneetha'
l=s.split()
l1=[]
for word in l:
    r=word[::-1]
    l1.append(r)
    output=" ".join(l1)
print(output)
---------------------------------

s='one two three four five six'
x=s.split()
i=0
l1=[]
while i<len(x):
    if i%2==0:
        l1.append(x[i])
        
    else:
        l1.append(x[i][::-1])

    i=i+1
    output=" ".join(l1)
print(output)
-----------------------------------------


s='navaneetha'
i=0
while i<len(s):
    print("chars present at even index :",s[i])
    i=i+2

i=1
while i<len(s):
    print("char present at odd index :",s[i])
    i=i+2
--------------------------------------------

x=input("enter a string : ")
x=x[::-1]
print(x)
-------------------------------------------

x=input("enter a string : ")
y=reversed(x)
y="".join(y)
print(y)
------------------------------------------

x=input("enter a string :")
output=" "
i=len(x)-1
while i>=0:
    output=output+x[i]
    i=i-1
print(output)
---------------------------------------

x=input("enter a string : ")
l=x.split()
l1=l[::-1]
y=" ".join(l1)
print(y)
---------------------------------------

x=input("enter a string : ")
l=x.split()
l1=[]
for word in l:
    r=word[::-1]
    l1.append(r)
print(l1)
----------------------------------------

x=input("enter a string : ")
l=x.split()
l1=[]
i=0
while i<len(l):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
output=" ".join(l1)
print(output)
------------------------------------------

x=input("enter a string : ")
l=x.split()
l1=[]
i=0
while i<len(l):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
    y=" ".join(l1)
print(y)
-------------------------------------------

#merge two strings alternatively

s1='navaneetha'
s2='yamini'
output=''
i,j=0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
print(output)
----------------------------------------

s='a1v3b5'
alphabets=[]
digits=[]
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
output="".join(sorted(alphabets)+sorted(digits))
print(output)
---------------------------------------

x='bdfgyf'
print(sorted(x))

#o/p:['b', 'd', 'f', 'f', 'g', 'y']
------------------------------------------

s='aaaabbbccz'
d={}
for i in s:
    d[i]=s.count(i)
print(d)
k=[]
for j,m in d.items():
    l=j+str(m)
    print(l,end="")
-----------------------------------------
'''
s='aaaabbbccz'
previous=s[0]
output=''
c=1
i=1
while i<len(s):
    if s[i]==previous:
        c=c+1
    else:
        output=output+str(c)+previous
        previous=s[i]
        c=1
    if i==len(s)-1:
        output=output+str(c)+previous
    i=i+1
print(output)
    




















        



































































































































































    






















        
               



































































            



















    











































































    










    













    
    
    























































        
        
    
































































