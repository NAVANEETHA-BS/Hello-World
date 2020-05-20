
import os

def main():
    print("welcome to tecno game station")
    print("main menu")
    print("main menu")
    print("1.sign in")
    print("2.sign up")
    print("3.exit")

def register():
    uname=input("enter name : ")
    upassword=input("enter password : ")
    phone_no=(input("enter phone number : "))
    email=input("enter email : ")
    #rec=sname+spassword+phone_no+email
    #print(rec)
    
    with open("p2.txt","w") as x:
        x.write(sname)
        x.write(spassword)
        x.write(phone_no)
        x.write(email)
    main()
    option()

    signin()
    if (sname and spassword) is (uname and upassword):
        print("you are a valid user")
        
    else:
        print("you are not a valid user")

def signin():
    sname=input("enter name : ")
    spassword=input("enter password : ")
    #check()
    #main()
    #option()
    #os.system('cls')
    
def exit():
    print("Thank you for your Interest")
    main()
    #option()
    
def option():
    option=int(input("enter 'option' to proceed : "))
    if option==2:
        register()
    elif option==1:
        signin()
    else:
        exit()


    #if uname==sname and upassword==spassword:
        #print("you are a valid user")
    #else:
        #print("you are not a valid user")

main()
option()
    
    
