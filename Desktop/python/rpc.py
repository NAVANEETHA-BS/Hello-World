#scissors,rock,paper game

import sys
import random
x=['Ramya','Nikitha','Sravanthi','Jayaraj','Sailaja','Vijitha','Navaneetha']

player1=input("Enter player1 name : ")
player2=input("Enter player2 name : ")

if player1 not in x:
    print("Invalid player1 name. ")
    sys.exit()
if player2 not in x:
    print("Invalid player2 name. ")
    sys.exit()

p1_one_score=0
p1_two_score=0

values=['Rock','Paper','Scissors']

i=1

def main() :
    global p1_one_score
    global p1_two_score
    global p1_one
    global p1_two
    print("Player 1 turn--To play type 'play'")
    p1_one=input(">>>")
    if p1_one=="play":
        p1_one_ans=random.choice(values)
        print(p1_one_ans)
    print("Player 2 turn--To play type 'play'")
    p1_two=input(">>>")
    if p1_two=="play":
        p1_two_ans=random.choice(values)
        print(p1_two_ans)

    if p1_one_ans=="Rock" and p1_two_ans=="Scissors" :
        p1_one_score+=1
        print("In this round player 1 is the winner")
    elif p1_one_ans=="Scissors" and p1_two_ans=="Rock":
        p1_two_score+=1
        print("In this round, player 2 is the winner")
    elif p1_one_ans=="paper" and p1_two_ans=="Rock":
        p1_one_score+=1
        print("In this round, player 1 is the winner")
    elif p1_one_ans=="Rock" and p1_two_ans=="Paper":
        p1_two_score+=1
        print("In this round, player 2 is the winner")
    elif p1_one_ans=="Scissors" and p1_two_ans=="Paper":
        p1_one_score+=1
        print("In this round, player 1 is the winner")
    elif p1_one_ans=="Paper" and p1_two_ans=="Scissors":
        p1_two_score+=1
        print("In this round player 2 is the winner")
    else:
        print("In this round game is tie")

while i<=5:
    main()
    i+=1

print("After 5 rounds,player1 score is :",p1_one_score)
print("After 5 rounds,player2 score is :",p1_two_score)

if p1_one_score>p1_two_score:
    print("player 1",p1_one,"is the winner, Congratulations!")
elif p1_one_score<p1_two_score:
    print("player 2",p1_two,"is the winner, Congratulations!")
else:
    main()
    if p1_one_score>p1_two_score:
        print("player 1",p1_one,"is the winner, congratulations!")
    elif p1_one_score<p1_two_score:
        print("player 1",p2_one,"is the winner, congratulations!")
