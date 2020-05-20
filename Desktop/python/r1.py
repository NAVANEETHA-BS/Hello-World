import random
score1=0
score2=0
plist=['r','shravanthi','nikitha','n','jayraj','sailaja']
p1=input("enter a player 1 : ")
p2=input("enter a player 2 : ")

if p1 in plist:
    if p2 in plist:
        print("valid player,plz continue playing ")
    else:
        print("plz enter valid player")
i=1
while i<=5:
    i+=1
    x=['r','s','p']
    a=input("player 1 type play to play  :")
    if a=="play":
        b=random.choice(x)
        print(b)

    c=input("player 2 type play to play  :")


    if c=="play":
         d=random.choice(x)
         print(d)
    if b=="r" and d=="s":   
        score1+=1
        print("player1 score is", score1)
    elif b=="r" and d=="p":
        score2+=1
        print("player2 score is", score2)
    elif b=="p" and d=="s" :   
        score2+=1
        print("player 2 score is", score2)
    elif b=="p" and d=="r" :   
        score1+=1
        print("player 1  score is", score1)
    elif b=="s" and d=="r" :    
        score2+=1
        print("player 2  score is", score2)
    elif b=="s" and d=="p" :
        score1+=1
        print("player 1 score is", score1)
    elif b==d:
        print("game tied,play again ")

if score1>score2:
    print("player1 won the game ")
else :
    print("player2 won the game ")
   

