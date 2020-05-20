'''
p=[]
file=open("words.txt","r")
y=file.readlines()
for l in y:
    #print(i,y[i])
    print()

text=input("enter text : ")
print(text)
p.append(text)
print(p)
for j in p:
    j=j.split()
    print(j)
    k=j[-1]
    print(k)
    n=k[:3:1]
    print(n)
    #for n in k:
        #m=n[:3]
        #print(m)
for i in range(len(y)):
    print(i,y[i])
    z=l[:3:1]
    print(z)
    if n==z:
        print(z)
--------------------------------------------------------------


d={}
j=1
data=input("enter data : ")
data1=data.split()
x=open("text.txt","r") 
y=x.readlines()

while data1[-1]!="":
    k=data1[-1]
    for i in y:
        if i[:len(k)]==k:
            d[j]=i
            print(str(j)+" "+i)
            j=j+1
    m=int(input("enter number to replace : "))
    data1=data1[:-1]
    a=""
    for i in data1:
        a=a+" "+i
    q=a+" "+d[m]
    print(q)
    r=input()
    q=q+" "+r
    print(q)
    q=q.split()
        
-----------------------------------------------------------

j=1
d={}
x=open("text.txt","r")
x=x.readlines()
#print(x)  ['neetha\n', 'new\n', 'not\n', 'nothing\n', 'notable\n', 'banana\n']
y=input("enter a data : ")
y=y.split()
#print(y)  ['my', 'name', 'is', 'ge']

while y[-1]!="":
    l=y[-1]
    for i in x:
        if i[:len(l)]==y[-1]:
            d[j]=i
            print(str(j)+":"+i)
            j=j+1
    m=int(input("enter data to replace : "))
    y=y[:-1]
    a=""
    for i in y:
        a=a+" "+i
    q=a+" "+d[m]
    print(q)
    p=input()
    q=q+" "+p
    print(q)
    y=q.split()
-------------------------------------------------------------

j=1
d={}
x=input("enter data : ")
x=x.split()

y=open("text.txt","r")
y=y.readlines()
while x[-1]!="":
    k=x[-1]
    for i in y:
        
        if i[:len(k)]==k:
            d[j]=i
            print(str(j),":",i)
            j=j+1
    m=int(input("enter numner to replace : "))
    x=x[:-1]
    a=''
    for i in x:
        a=a+" "+i
    q=a+" "+d[m]
    print(q)
    n=input()
    q=q+" "+n
    print(q)
    x=q.split()
 ---------------------------------------------------------
 '''
x=[5,3,4,7,1]
a=x[0]
b=x[0]
for i in x:
    if i>a:
        a=i
        print(a)
    if i<b:
        b=i
        print(b)
    
    






















































