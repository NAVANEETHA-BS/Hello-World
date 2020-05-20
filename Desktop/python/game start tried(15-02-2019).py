import random

n=int(input("enter number of times to play the game : "))
count1=0
count2=0
for i in range(1,n+1):
    print("player1 to play the game: ")
    x=random.randint(1,7)
    print(x)
    count1=count1+x
    print("player2 to play the game: ")
    y=random.randint(1,7)
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

