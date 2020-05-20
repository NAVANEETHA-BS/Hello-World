#write a python program to read data from a given file
'''
x=open("a1.txt","w")
x.write("hello, python\n")
x.write("python is simple\n")
x.write("python is easy\n")
x.close()
or

x=open("a1.txt","r")
k=x.read()
print(k)


#write a python program to find size of the given file
#import os
x=open("a1.txt","r")

#print(os.path.getsize("a1.txt"))
k=x.read()
print("size of the given file",len(k))

#print(x)


#write a python program to find total number of lines of the given file

x=open("a1.txt","r")
k=x.readlines()
print("total no of lines : ",len(k))
#print(k)


#write a python program to display nth line from a given file
x=open("a1.txt","r")
n=int(input("enter a nth line to open : "))
y=x.readlines()
l=len(y)
print(l)

if l<n:
    print(y[n-1])
else:
    print("out of size")


a=['python','django','perl','java','unix','dba','aws','devops']
fn=input("Enter a filename to create : ")
x=open(fn,"w")
for i,j in enumerate(a):
    x.write(str(i+1)+"."+j)
    x.write("\n")
x.close()
print("created.")



#write python program to count total number of empty lines in a given file


x=open("a1.txt","r")
#cnt=0
y=x.readlines()
print(y)
print(y.count('\n'))

        


#6)write python program display 1st five and last five lines from a given file

with open("a1.txt","r") as x:
    k=x.readlines()
    z=k[:1]+k[-1:]
    print(z)



#7)write a python program display first 10 characters and last 10 characters
#from a given file

with open("a1.txt","r") as x:
    k=x.read()
    #print(k)
    z=k[:5]+k[-6:]
    print(z)
    


#8)write a python program count how many times the given word occured in a
#given file

n=input("enter a word in a file : ")
with open("a1.txt","r") as x:
    k=x.read()
    if n in k:
        print(k.count(n))
    else:
        print("given word doesn't exist in the file")
        
   

#9)write a python program to display unique lines from a given file

with open("a1.txt","r") as x:
    
    y=x.readlines()
    z=set(y)
    print(z)
'''

#10)write a python delete a given word from a given file

n=input("enter any word to delete : ")
with open("a1.txt","r") as x:
    y=x.read()
    z=y.replace(n," ")
    print(z)
    





























