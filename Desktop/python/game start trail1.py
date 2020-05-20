
import random
'''
n=int(input("enter number of times to play : "))
for i in range(1,n+1):
'''
#n=int(input("enter number of times to play the game : "))
#count1=0
#count2=0
ans=input("enter 'play' to play the game : ")
if ans=='play':
#for i in range(1,n+1):

    x=random.randint(1,6)
    print("player1 to play the game for dice 1:=",x)
    
    y=random.randint(1,6)
    print("player1 to play the game for dice 2:=",y)
    
    if x==y:
        x=x+y
        playagain()
    else:
        x=x+y
        print("total score for dice 1 : ",x)


    x=random.randint(1,6)
    print("player2 to play the game for dice 1:=",x)
    
    y=random.randint(1,6)
    print("player2 to play the game for dice 2:=",y)
    

    if x==y:
        playagain()
    else:
        x=x+y

    print("total score for dice 2 : ",x)


def playagain():
    print("both scores are equal,play again")
    z=random.randint(1,6)
    print("player 1 score for dice new dice : ",z)
    x=x+z
print("total score for dice : ",x)
    

'''
import random

n=int(input("enter number of times to play : "))
for i in range(1,n+1):

n=int(input("enter number of times to play the game : "))
count1=0
count2=0


#n=int(input("enter number of times to play : "))
for i in range(1,n+1):
    print("player1 to play the game: ")
    x=random.randint(1,6)
    print(x)
    count1=count1+x
    print("player2 to play the game: ")
    y=random.randint(1,6)
    print(y)
    count2=count2+y
print("count1=",count1)
if count1%2==0:
    print("count1 is an even number",count1)
    count1=count1+10
    print("total score of player 1 : ",count1)
else:
    print("count1 is an odd number",count1)
    count1=count1-5
    print("total score of player 1 : ",count1)
 
print("count2=",count2)
if count2%2==0:
    print("count2 is an even number",count2)
    count2=count2+10
    print("total score of player 2 : ",count2)
else:
    print("count2 is an odd number",count2)
    count2=count2-5
    print("total score of player 2 : ",count2)

if count1>count2:
    print("CONGRATULATIONS,player1 won the game")
else:
    print("CONGRATULATIONS,player2 won the game")

'''
