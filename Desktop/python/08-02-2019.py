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
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open(fn,"r") as x:
            y=x.readlines()
            for i in y:
                if i!="\n":
                    print(i)

                    (DOUBT)



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




#31)write a python script accept file and reverse the file contents in sorted
#order

import os
fn=input("enter a filename : ")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open(fn,"r") as x:
            y=x.read()
            #for i in y:
            print((y[::-1]))
            
            (DOUBT)

'''

#34)write a python script accept a file and string and count total no
# of occorences

import os
fn=input("enter a filename : ")
str=input("enter a string : ")
if os.path.exists(fn):
    if os.path.isfile(fn):
        with open(fn,"r") as x:
            
            y=x.read()
            z=y.split(" ")
            cnt=0
            for i in z:
                print(i.count(str))
                '''
                if str==i:
                    cnt=cnt+1
                    print(cnt)
                
                '''
                

             
         
























                    





            







                











            
        
    

 
