import os,sys,time,random

def check(x,y):
    for i in y:
        i=i.split(",")
        if i[0]==x:
            print(x,"welcome to play the game,..")
            playgame(x)
            break

    else:
        print("sorry,you are not a valid player",x)
        x=input("enter a player name : ")
        check(x,y)
        #register()



        

def signin():
    sname1=input("enter username 1 : ")
    sname2=input("enter a username 2: ")
    with open("a5.txt","r") as x:
        k=x.readlines()
    check(sname1,k)
    check(sname2,k)


def checkuser(a):
    if os.path.exists("a5.txt") and os.path.isfile("a5.txt"):
        with open("a5.txt","r") as x:
            k=x.readlines()
            user=[]
            for i in k:
                i=i.split(",")
                user.append(i[0])
            if a not in user:
                return a
            else:
                print(a,"user already exist")
                print("plz choose other than this user",user)
                name=input("enter your name : ")
                a=checkuser(name)
                return a
    else:
        return a
    

def register():
    uname=input("enter new name : ")
    un=checkuser(uname)
    upassword=input("enter a password : ")
    ph_no=input("enter a phone number : ")
    email=input("enter a email : ")
    rec=un+","+upassword+","+ph_no+","+email+"\n"
    with open("a5.txt","a") as x:
        x=x.write(rec)
    print("registered successfully")
    time.sleep(5)
    main()   

def main():
    print("welcome to tecno game station")
    print("main menu")
    print("1.sign in")
    print("2.sign up")
    print("3.exit")
    ans=int(input("enter option to proceed : "))
    
    if ans==1:
        signin()

    elif ans==2:
        register()

    else:
        print("thank you for your interest")
        sys.exit()

if __name__=="__main__":
    main()


def playgame(x):
    pl_one_tot=0

    pl_two_tot=0
    n=int(input("enter no of rounds to play the game : "))
    for i in range(1,n+1):
          
        
        player1=rolldice(pl_tot)
        pl_one_tot=pl_one_tot+player1
        player2=rolldice(pl_tot)
        pl_two_tot=pl_two_tot+player2
        if pl_one_tot==pl_two_tot:
            tie(pl_tot)
            pl_one_tot=pl_one_tot+pl_tot
            pl_two_tot=pl_two_tot+pl_tot

def tie(pl_tot):
    ans=input("enter type 'roll' to play the game : ")
    if ans=="roll":
        d1=random.randint(1,6)
        d2=random.randint(1,6)
        print("score : ",d1,d2)
        pl_tot=d1+d2
        if d1==d2:
            pl_tot=d1+d2
            print("congatulations, you got another chance to roll the dice")
            ans=input("enter type 'roll' to play the game : ")
            if ans=="roll":
                d=random.randint(1,6)
                print("extra score : ",d)
                pl_tot=pl_tot+d
                print(pl_tot)
    return pl_tot


def rolldice(pl_tot):
    ans=input("enter type 'roll' to play the game : ")
    if ans=="roll":
        d1=random.randint(1,6)
        d2=random.randint(1,6)
        print("score : ",d1,d2)
        pl_tot=d1+d2
        
        if d1==d2:
            pl_tot=d1+d2
            print("congatulations, you got another chance to roll the dice")
            ans=input("enter type 'roll' to play the game : ")
            if ans=="roll":
                d=random.randint(1,6)
                print("extra score : ",d)
                pl_tot=pl_tot+d
                print(pl_tot)
            return pl_tot
        #pl_one_tot=pl_one_tot+pl_tot
        #pl_two_tot=pl_two_tot+pl_tot
            
            
            
            
        
    
        
    






    
