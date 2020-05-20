import os,sys,time,random

def RollDice(x,total):
    ans=input("Type 'roll' to dice : ")
    if ans=='roll':
        a=random.randint(1,6)
        b=random.randint(1,6)
        print("Dice 1 and Dice 2 : ",a,b)
        total=a+b
        if a==b:
            print("Wow!you gotone more chance to dice,..")
            ans=input("Type 'roll' to dice : ")
            if ans=='roll':
                c=random.randint(1,6)
                print("Extra Dice : ",c)
                total+=c
        return total

def TopScoresList(fname):
    with open(fname,"r") as x:
        k=x.readlines()
    names=[]
    for i in k:
        i=i.rstrip("\n")
        i=i.split(",")
        #names[i[0]]=i[1]
        names.append([i[1],i[0]])
        scores=[]
        for i in names:
            scores.append(i[0])
        scores=sorted(set(scores),reverse=True)
    if len(k)<=5:
        #y=sorted(set(names.values()),reverse=True)
        for i in scores:
            for n in names:
                if i==n[0]:
                    print(n[1],":",n[0])
    else:
        for i in scores[:5]:
            for n in names:
                if i==n[0]:
                    print(n[1],":",n[0])
                 
'''

        for i in y:
            for n,m in names.items():
                if i==m:
                    print(n,":",i)
    else:
        y=sorted(set(na
        mes.values()),reverse=True)
        for i in y[:5]:
            for n,m in names.items():
                if i==m:
                    print(n,":",i)

'''

def SaveToFile(pname,total):
    if os.path.exists("winners.txt") and os.path.isfile("winners.txt"):
        with open("winners.txt","a") as x:
            rec=pname+","+str(total)+"\n"
            x.write(rec)
        TopScoresList("winners.txt")
    else:
        with open("winners.txt","w") as x:
            rec=pname+","+str(total)+"\n"
            x.write(rec)
        TopScoresList("winners.txt")

def tie(x,y):
    print("Both got same score, let's roll dice again")
    ans=input("player 1,Type 'roll' to dice : ")
    
    if ans=='roll':
        a=random.randint(1,6)
        print("player 1 dice : ",a)
    ans=input("player 2,Type 'roll' to dice : ")
    if ans=='roll':
        b=random.randint(1,6)
        print("player 2 dice : ",b)
    if a>b:
        print("player 1",x,"won this game.congratulations!")
    elif a<b:
        print("player 2",y,"won this game.congratulations!")
    else:
        tie(x,y)

        

def playgame(x,y):
    p_one_total=0
    p_two_total=0
    print("welcome",x,"and",y,"to play game.All the best")
    for i in range(1,6):
        print("Round",i,"starts: ")
        p1=RollDice(x,p_one_total)
        p_one_total=p1+p_one_total
        p2=RollDice(y,p_two_total)
        p_two_total=p2+p_two_total
        print("After round",i,"total score of")
        print("player 1 ",x,"is : ",p_one_total)
        print("player 2 ",y,"is : ",p_two_total)
    print("After five rounds : ")
    print("player 1",x,"total is : ",p_one_total)
    print("player 2",y,"total is : ",p_two_total)
    if p_one_total%2==0:
        p_one_total+=10
    else:
        p_one_total-=5
    if p_two_total%2==0:
        p_two_total+=10
    else:
        p_two_total-=5
    print("player 1",x,"final score : ",p_one_total)
    print("player 2",y,"final score : ",p_two_total)
    if p_one_total>p_two_total:
        print("player 1",x,"won the game.congratulations!")
        SaveToFile(x,p_one_total)
    elif p_one_total<p_two_total:
        print("player 2",y,"won the game.congratulations!")
        SaveToFile(y,p_two_total)
    else:
        tie(x,y)


def check(x,y):
    for i in y:
        i=i.split(",")
        if i[0]==x:
            print(x,"welcome to play the game,..")
            #playgame(x,y)
            break

    else:
        print("sorry,you are not a valid player",x)
        x=input("enter a player name : ")
        check(x,y)
        #register()


def signin():
    with open("a5.txt","r") as x:
        k=x.readlines()
    sname1=input("enter username 1 : ")
    check(sname1,k)
    sname2=input("enter a username 2: ")
    check(sname2,k)
    playgame(sname1,sname2)


def checkuser(a):
    if os.path.exists("a5.txt") and os.path.isfile("a5.txt"):
        with open("a5.txt","r") as x:
            k=x.readlines()
            users=[]
            for i in k:
                i=i.split(",")
                users.append(i[0])
            if a in users:
                #return a
            #else:
                print(a,"user already exist")
                print("plz choose other than this user",users)
                uname=input("enter your name : ")
                a=checkuser(uname)
                return a
            else:
                return a
    else:
        return a
    

def register():
    uname=input("enter new name : ")
    uname=checkuser(uname)
    upassword=input("enter a password : ")
    ph_no=input("enter a phone number : ")
    email=input("enter a email : ")
    rec=uname+","+upassword+","+ph_no+","+email+"\n"
    with open("a5.txt","a") as x:
        x.write(rec)
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
