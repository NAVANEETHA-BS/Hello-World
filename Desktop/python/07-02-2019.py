'''
#18)write a program accept a file and check the given file exist or not

import os
fn=input("enter a filename : ")
if os.path.exists(fn):
    #if os.path.isfile("fn"):
    print("file exist")
else:
    print("file doesn't exist")


#19)write a program to accept a file and display its file type
import os
fn=input("enter a filename : ")
if os.path.isfile(fn):
    print("it is a file ")
elif os.path.isdir(fn):
    print("it is a directory ")



#20)write a program accept a directory and count total no. of files

import os
fn=input("enter a dirname : ")
if os.path.exists(fn):
    print("directory exist")
    if os.path.isdir(fn):
        print("it is a directory")
        print(os.getcwd())
#[C:\Users\Neetha\Desktop\python]-it is current dir
        #cnt=os.listdir(fn)
        #print(len(cnt))
         #print(len(os.listdir(fn)))

'''


            
        














