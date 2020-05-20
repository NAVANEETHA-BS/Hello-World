d={}
j=1
n=input("enter a passage : ").split()
x=open("words.txt","r")
data=x.readlines()
while n[-1]!="":
    l=n[-1]
    for i in data:
        if i[:len(l)]==1:
            d[j]=i
            print(j," ",i)
            j=j+1
    m=int(input("enter number to replace : "))
    n=n[:-1]
    a=""
    for i in n:
        a=a+" "+i
    n=a+" "+d[m]
    print(n)
    z=input()
    n=n+" "+z
    print(n)
    n=n.split()
