'''
n=input("enter words : ")
n=n.split(" ")
for j in n:
    print(j)
    
with open("sample.txt","r") as x:
    for i in x:
        if n==i[0]:
            print(i)

-------------------------------------------------------------            


n=input("enter words : ")
n=n.split(" ")
with open("sample.txt","r") as x:
    y=x.readlines()
    for i in n:
        if i in y:
            print(y)
    
------------------------------------------------------

import re
x=input("enter data : ")
x=x.split(" ")
#for i in x:
print(x[-1])
x[-1]=str(x[-1])
print(type(x))
with open("sample.txt","r") as f:
    y=f.read()
    for j in y:
        print(j)
        j=str(j)
        print(type(j))
        if x[-1] in y:
            print(y)
----------------------------------------------------

x=input("enter data : ")
x=x.split()
#for i in x:
print(x)
for i,j in enumerate(x):
    print(i,j)
#print(x[-1])
#for i in x[-1]:
    #print(i)

    #print(i)
    #print(type(i))
#print(x[-1])

  

with open("sample.txt","r") as f:
    f=f.read()
    f=f.split()
    print(f)
    for m,n in enumerate(f):
        print(m,n)
    #for j in f:
        #if j in x[-1]:
            #print(j)
        #print(j[::1])
    #print(type(f))
        if n[0:2:]==j[0:2:]:
            print(n)
    print()
--------------------------------------------


x=input("enter data : ")
x=x.split()
#for i in x:
#print(x)
for i,j in enumerate(x):
    print()
    #print(i,j)
#print(x[-1])
#for i in x[-1]:
    #print(i)

    #print(i)
    #print(type(i))
#print(x[-1])

  

with open("sample.txt","r") as f:
    f=f.read()
    f=f.split()
    #print(f)
    for m,n in enumerate(f):
        #print(m,n)
    #for j in f:
        #if j in x[-1]:
            #print(j)
        #print(j[::1])
    #print(type(f))
        if n[0:2:]==j[0:2:]:
            print(n)
    print()
-----------------------------------------------------------



x=input("enter data : ")
x=x.split()
for i,j in enumerate(x):
    print()
    
with open("sample.txt","r") as f:
    f=f.read()
    f=f.split()
    for m,n in enumerate(f):  
        if n[0:2:]==j[0:2:]:
                print(n)
            
            
    print()

-------------------------------------------------------
'''
x=input("enter data : ")
x=x.split()
for i,j in enumerate(x):
    print()
    
with open("sample.txt","r") as f:
    f=f.read()
    f=f.split()
    for m,n in enumerate(f):
        index=1
        if n[0:2:]==j[0:2:]:
            index+=1
            #print(index,n)
            for i in range(index):
                #print()
                print(str(i)+"."+n)
                #index+=1
    print()





















































    
