'''
#21)write a program accept a directory and count total no. of files
# and directories


import os
fn=input("enter a dirname : ")
cntd=0
cntf=0
if os.path.exists(fn):
    if os.path.isdir(fn):
         p=os.listdir(fn)
         os.chdir(fn)
         
         for i in p:
            if os.path.isdir(i):
                cntd+=1
            if os.path.isfile(i):
                cntf+=1
print("cntf=" ,cntf)
print("cntd=" ,cntd)
            
'''
#22)write a program accept a directory and display only all .py files

import os
fn=input("enter a dirname : ")
if os.path.exists(fn):
    if os.path.isdir(fn):
        os.chdir(fn)
        #print(len(os.listdir(fn)))
        p=os.listdir(fn)

   # print(p)
        for i in p:
            if i.endswith('.py'):
                print(i)

                    
            
        














            
                 
             
