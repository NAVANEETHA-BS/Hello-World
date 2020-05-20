
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


a=int(input("enter number of rounds to play the game : "))

count1=0
count2=0
i=1
while i<=a:

    ans1=input("enter 'roll' to play the game : ")
    if ans1=="roll":
        #playagain()
        x=random.randint(1,6)
        print("player 1 score for dice 1 : ",x)

#ans2=input("enter 'roll' to play the game : ")
#if ans2=="roll":
        y=random.randint(1,6)
        print("player 1 score for dice  2 : ",y)
    
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
    print("overall score for player 1 : ",count1)




    ans4=input("enter 'roll' to play the game : ")
    if ans4=='roll':
        #playagain()
        p=random.randint(1,6)
        print("player 2 score for dice 1 : ",p)

#ans5=input("enter 'roll' to play the game : ")
        
#if ans5=='roll':
        q=random.randint(1,6)
        print("player 2 score for dice 2 : ",q)

        if p!=q:
            p=p+q
            print(p)
        else:

            p=p+q
            ans6=input("enter 'roll' to play again : ")
            n=random.randint(1,6)
            print("player 2 score for rolled again dice : ",n)
            p=p+n
    print("overall score for round 1 for player 2 : ",p)
    count2=count2+p
    print("overall score of player 2 : ",count2)
    i=i+1


        
if count1%2==0:
    count1+=10
    print("final result for player 1 : ",count1)


else:# count1%2==1:
    count1-=5
    print("final result for player 2 : ",count1) 

if count2%2==0:
    count2+=10
    print("final result for player 1 : ",count2)

else:# count2%2==1:
    count2-=5
    print("final result for player 2 : ",count2)

#if count1==count2:
    #playagain()
    
if count1>count2:
    print("CONGRATULATIONS, player 1 won the game")
else:
    print("CONGRATULATIONS, player 2 won the game")

    








    




