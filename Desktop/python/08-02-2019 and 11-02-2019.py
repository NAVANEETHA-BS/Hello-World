'''
#23)write a program accept a directory and display all empty files

import os
fn=input("enter a dirname : ")

if os.path.exists(fn):
    if os.path.isdir(fn):
        os.chdir(fn)
        print(os.getcwd())
        p=os.listdir(".")
        for i in p:
            if os.path.isfile(i):
                size=os.path.getsize(i)
                if size==0:
                    print(i)



#24)write a python script accept a file and count total no. of characters,
 # total no of words and total no. of lines

import os
fn=input("enter a filename : ")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open(fn,"r") as x:
            data=x.readlines()
            print("total no. of lines : ",len(data))
            print("total no. of chars :",os.path.getsize(fn))
            wcnt=0
            for i in data:
                i=i.split(" ")
                wcnt=wcnt+len(i)
            print("Total no. of words:",wcnt)



#25)write a python script accept a file and a string and delete the
# string from a file

import os
fn=input("enter a file : ")
str=input("enter a string ")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open(fn,"r") as x:
            y=x.read()

            if str in y:
                z=y.replace(str," ")
                print(z)



'''

#26)write a python script accept a file and string, if given string found
# then read data from given string to end of the file

import os
fn=input("enter a filename : ")
str=input("enter a string ")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open(fn,"r") as x:
            y=x.read()
            #y=y.find("python")
            z=y[6::1]
            print(z)

'''

#27)write a python script to delete duplicate lines from a file

import os
fn=input("enter a filename : ")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open(fn,"r") as x:
            y=x.readlines()
            z=set(y)
            print(z)


#28)write a python script to delete empty lines fron a given file

import os
fn=input("enter a filename : ")
if os.path.exists(fn) and os.path.isfile(fn):
    with open(fn,"r") as x:
        y=x.readlines()
        for i in y:
            if i!='\n':
            #z=i.replace("\n","")
            #z=i.replace('\n'," ")
                print(i)

                    



#29)write a python script accept a file and display each line last word

import os
fn=input("enter a filename : ")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open(fn,"r") as x:
            y=x.readlines()
            for i in y:
                i=i.split()
                print(i[-1])


#30)write a python script accept a file and display file contents in sorted order

import os
fn=input("enter a filename : ")
if os.path.exists(fn) and os.path.isfile(fn):
    with open(fn,"r") as x:
        y=x.read()
        y=y.split()
        z=sorted(y)
        print(z)
    



#31)write a python script accept file and reverse the file contents in sorted
#order

import os
fn=input("enter a filename : ")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open(fn,"r") as x:
            y=x.read()
            #for i in y:
            y=y[::-1]
            #print(y)
            y=y.split()
            z=sorted(y)
            print(z)
            
            



#34)write a python script accept a file and string and count total no
# of occurences

import os
fn=input("enter a filename : ")
str=input("enter a string : ")
if os.path.exists(fn) and os.path.isfile(fn):
    with open(fn,"r") as x:
            y=x.read()
            z=y.split()
            cnt=0
            for i in z:
                #w=z.count(i)
                #print(w)
                
                if str==i:
                    cnt=cnt+1
            print(cnt)
            


#39)write a python script accept a directory and count total no. of files and
#total no. of directories

import os
fn=input("enter a dirname : ")
fcnt=0
dcnt=0
if os.path.exists(fn):
    if os.path.isdir(fn):
        p=os.listdir(fn)
        os.chdir(fn) 
        for i in p:
            if os.path.isdir(i):
                dcnt+=1
            if os.path.isfile(i):
                fcnt+=1
print("total no. of files : ",fcnt)
print("total no. of dirs : ",dcnt)



#40)write a python script accept a directory and list which file are
#sizes more than 1000 bytes

import os
fn=input("enter a dirname : ")
if os.path.exists(fn):
    if os.path.isdir(fn):
        p=os.listdir(fn)
        os.chdir(fn)
        for i in p:
            if os.path.isfile(i):
                if os.path.getsize(i)>=1000:
                    print(i)



#41)write a program to accept two files and display common records in both files

import os
fn1=input("enter a filename1 : ")
fn2=input("enter a filename2 : ")
if os.path.exists(fn1) and os.path.isfile(fn1):
    if os.path.exists(fn2) and os.path.isfile(fn2):
        with open(fn1,"r") as x:
            n=x.readlines()
            n=set(n)
    #for i in n:
        with open(fn2,"r") as y:
            m=y.readlines()
            m=set(m)
    #for j in m:
        z=m & n
        print(z)
                                #else:
                                    #print("no common record in both the files")





#42)write a program to accept 2 files and display opposite records from both files

import os
fn1=input("enter a filename1 : ")
fn2=input("enter a filename2 : ")
if os.path.exists(fn1) and os.path.isfile(fn1):
    if os.path.exists(fn2) and os.path.isfile(fn2):
        with open(fn1,"r") as x:
            m=x.readlines()
            m=set(m)
    #for j in m:
        with open(fn2,"r") as y:
            n=y.readlines()
            n=set(n)
    #for i in n:
            z=m ^ n                #print(i)
            print(z)
                                    
                                    
 




#43)write a program accep 2 files and join horizontally with "-" delimiter

import os
fn1=input("enter a filename 1 : ")
fn2=input("enter a filename 2 : ")
if os.path.exists(fn1) and os.path.isfile(fn1):
    if os.path.exists(fn2) and os.path.isfile(fn2):
        with open(fn1,"r") as x:
            f1=x.readlines()
        with open(fn2,"r") as x:
            f2=x.readlines()
        l1=len(f1)
        l2=len(f2)
        temp=[]

        if l1>l2:
            for i in range(l2):
                k=f1[i].rstrip("\n")+"-"+f2[i]
                temp.append(k)
            temp.extend(f1[i+1:])
            print(temp)
        elif l1<l2:
            for i in range(l1):
                k=f1[i].rstrip("\n")+"-"+f2[i]
                temp.append(k)
            temp.extend(f2[i+1:])
            print(temp)
        else:
            for i in range(l2):
                k=f1[i].rstrip("\n")+"-"+f2[i]
                temp.append(k)
            print(temp)
            
        


#44)write a program to accept 2 files and check both file contents are same or not

import os
fn1=input("enter a filename1 : ")
fn2=input("enter a filename2 : ")
if os.path.exists(fn1) and os.path.isfile(fn1):
    if os.path.exists(fn2) and os.path.isfile(fn2):
        with open(fn1,"r") as x:
            n=x.readlines()
            n=set(n)
        with open(fn2,"r") as y:
            m=y.readlines()
            m=set(m)
                        #for i in n:
                            #for j in m:
            if n-m==m-n:                   
            
                                #if i==j:
                print("both the file contents are same")
            else:
                print("both file contents are not same")
                                



#45)write a program to accept a file and add "Tecnosoft" at end of the line
                                    
import os
fn=input("enter a filename : ")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open(fn,"r") as x:
            y=x.readlines()
            for i in y:
                z=i.rstrip("\n")
                #print(i+i.rstrip("\n")+" "+"Tecnosoft")
            print(i+z+" "+"Tecnosoft")



#38)write a python script accept 2 files and concatenate 2 files data
# and store into 3rd file

import os
fn1=input("enter a filename1 : ")
fn2=input("enter a filename2 : ")
fn3=input("enter a filename3 : ")
if os.path.exists(fn1) and os.path.isfile(fn1):
    if os.path.exists(fn2) and os.path.isfile(fn2):
        with open(fn1,"r") as x:
            m=x.readlines()
        with open(fn2,"r") as x:
            n=x.readlines()
            y=(m+n)
            #k=y.readlines()
        with open(fn3,"w") as x:
            x.writelines(y)

        



#35)write a python script create given no of directories in the current directory

import os
n=int(input("enter no. of directories to create : "))
for i in range(1,n+1):
    dn=input("enter directory name : ")
    os.mkdir(dn)



#33)write a python script accept a file and display frequency of words in dictionary format

import os
fn=input("enter a file name : ")
if os.path.exists(fn) and os.path.isfile(fn):

    with open(fn,"r") as x:
        y=x.read()
        #y=y.replace("\n"," ") ---this is compulsory
        z=y.split()
        d1={}
        for i in set(z):
            d1[i]=z.count(i)
        print(d1)
            

#36) write a python script to copy a file

import os
sf=input("enter a source filename : ")
tf=input("enter a target filename : ")
if os.path.exists(sf) and os.path.isfile(sf):
    with open(sf,"r") as x:
        k=x.read()
    with open(tf,"w") as x:
        x.write(k)
    print("file copied")
else:
    print("file not copied")


#37) write a python script to move a file

import os
sf=input("enter a source filename : ")
tf=input("enter a target filename : ")
if os.path.exists(sf) and os.path.isfile(sf):
    with open(sf,"r") as x:
        k=x.read()
    with open(tf,"w") as x:
        x.write(k)
        os.remove(sf)
    print("file moved")
else:
    print("file not moves")

 '''          
        
        
            
         
 
             
         
























                    





            







                











            
        
    

 
