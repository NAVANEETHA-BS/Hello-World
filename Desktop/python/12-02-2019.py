'''

import os,sys
dn=input("enter a directory name : ")
msg=input("enter greetings to send : ")
if os.path.exists(dn) and os.path.isdir(dn):
    os.chdir(dn)
    print(os.getcwd())
    x=os.listdir(dn)
    os.chdir(dn)
    print(os.getcwd())
    print(x)
    for i in x:
        if os.path.isfile(i):
            with open(i,"a") as o1:
                o1.write("\n**********************************\n")
                o1.write("happy radhasapthami")
                o1.write(msg)
                #o1.write(sys.arg[1])
                o1.write("\n**********************************\n")
        else:
            print("no such dir")


import os,sys
dn=input("enter a directory name : ")
if os.path.exists(dn) and os.path.isdir(dn):
    os.chdir(dn)
    x=os.listdir(dn)
    #os.chdir(dn)
    print(x)
    for i in x:
        if os.path.isfile(i):
            with open(i,"a") as o1:
                o1.write("\n*************************************\n")
                o1.write("happy radhasapthami")
                o1.write(sys.argv[1])
                o1.write("\n*************************************\n")
        else:
            print("no such dir")
        
 '''











