'''
#11)write a python program to write each and every line first and last words
#into another file with comma separator

x=open("a1.txt","r")
k=x.readlines()
f=open("a5.txt",'w')
for i in k:
    #print(i)
    y=i.split(" ")
    #print(y)
    z=y[0]+","+y[-1]
    print(z)
m=f.write(z)
f.close()
#print(m)



#12)write a python program  display all given word lines from a given file

w=input("enter a word to display the line : ")
x=open("a1.txt","r")
k=x.readlines()
for i in k:
    #print(i)
    if w in i:
        print(i)
else:
    print("given word doesn't exist")



#13)write a python program display which are the lines having exactly five
#words

x=open("a1.txt","r")
k=x.readlines()
for i in k:
    n=i.split(" ")
    #print(n)
    if len(n)==5:
        print(i)


#14)python program to display alternative lines from a file

x=open("a1.txt","r")
k=x.readlines()
for i in k:
    n=k[::2]
print(n)


#no need to close the file if we use with open() as x, otherwise we need to close
#15)write a python program to sort the given file contents

x=open("a1.txt","r")
k=x.readlines()
k.sort()
x.close()
y=open("b1.txt","w")
m=y.writelines(k)
y.close()



#16)write a python program swap each line first and last word and
#write into another file

x=open("a1.txt","r")
k=x.readlines()
f=open("a5.txt",'w')
for i in k:
    #print(i)
    y=i.split(" ")
    #print(y)
    y[0],y[-1]=y[-1],y[0]
    #z=y[0]+" "+y[-1]
    #m[0],m[-1]=m[-1],m[0]
    print(y)



#17)write a python program display which are the lines starting with
#"error" word in a given file

x=open("a1.txt","r")
k=x.readlines()
for i in k:
    y=i.split()
    if y[0]=="error":
        print(i)


'''









































        















