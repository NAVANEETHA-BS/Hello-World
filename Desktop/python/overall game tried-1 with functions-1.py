import os,sys,time,random

def check(x,y):
    for i in y:
        i=i.split(",")
        if i[0]==x:
            print(x,"welcome to play the game,..")
            break

    else:
        print("sorry,you are not a valid player",x)
        x=input("enter a player name : ")
        #check(x,y)
        register()
        

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





#count1=0
def playgame():
    #user1=[]
    #count1=0
    
    ans1=input("enter 'roll' to play the game : ")
    #count1=0
    if ans1=="roll":
        count1=0
        x=random.randint(1,6)
        y=random.randint(1,6)
        print("player 1 score for dice 1 and dice  2 : ",x, y)
    
        if x!=y:
            x=x+y
            print(x)
        else:
            x=x+y
            ans3=input("enter 'roll' to play again : ")
            z=random.randint(1,6)
            print("player 1 score for rolled again dice : ",z)
            x=z+x
    
        print("overall score for round 1 for player 1 : ",x)
    count1=count1+x
        #user1.append(count1)     
    print("overall score for player 1 : ",count1)
       

    

def playagain():
    ans1=input("enter 'roll' to play the game : ")
    if ans1=="roll":
        a=random.randint(1,6)
        b=random.randint(1,6)
    print("player 1 score for dice 1 and dice  2 : ",a, b)
    count1+=a
    count2+=b
    print("final score for repeated dice : ",count1,count2)

    



a=int(input("enter number of rounds to play the game : "))
i=1
while i<=a:
    for i in range(a+1):
        count1=0
        
        playgame(pl_one,pl_two)
    
        
    
i=i+1
#print("final score for player 1 : ",count1)
#print("final score for player 2 : ",count2)

if count1==count2:
    playagain()
    
else:
    print("overall score for dice1 and dice2 : ",count1,count2)














