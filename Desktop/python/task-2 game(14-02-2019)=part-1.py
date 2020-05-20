import os,sys,time

def check(x,y):
    for i in y:
        i=i.split(",")
        if i[0]==x:
            print("HI",x,"welcome to play the game,...")
            break
    else:
        print("sorry",x,",you are not a registered player")
        x=input("enter a player name : ")
        check(x,y)

def login():
    pl1=input("enter a player name 1 : ")
    pl2=input("enter a player name 2 : ")
    with open("users.txt") as x:
        k=x.readlines
        check(pl1,k)
        check(pl2,k)
    
def checkuser(a):
    if os.path.exists("users.txt") and os.path.isfile("users.txt"):
        with open("users.txt","r") as x:
            k=x.readlines()
        users=[]
        for i in k:
            i=i.split(",")
            users.append(i[0])
        if a not in users:
            return a

        else:
            print("user",a,"already exists")
            print("plz choose otherthan this users",users)
            Name=input("Enter your name : ")
            a=checkuser(Name)
            return a
    else:
        return a

def register():
    uname=input("enter name: ")
    un=checkuser(uname)
    pwd=input("enter password : ")
    phno=input("enter phno : ")
    email=input("enter email : ")
    rec=un+","+pwd+","+phno+","+email+"\n"

    with open("users.txt","a") as x:
        x.write(rec)
    print("registered successfully.")
    time.sleep(5)
    main()
def main():
    os.system('cls')
    print("\t\t welcome to tecnosoft game station")
    print("\t"+"*"*50)
    print()
    print()
    print("\t\t\t main menu\n")
    print("\t\t\t 1.login")
    print("\t\t\t 2.Register")
    print("\t\t\t Exit\n")
    ans=int(input("Enter option[1-3]:"))
    if ans==1:
        os.system('cls')
        print("\t\t welcome to Tecnosoft Game Station")
        print("*"*60)
        print()
        print()
        login()
    elif ans==2:

        os.system('cls')
        print("\t\t welcome to tecnosoft game station")
        print("*"*60)
        print()
        print()
        register()
    else:
        print("thank you")
        sys.exit()

if __name__=="__main__":
    main()
    

