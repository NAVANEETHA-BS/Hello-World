'''
#1)write a python program to find whether a given number is even or odd recursively

def even(i):
    if i<len(x):
        if x[i]%2==0:
            print(x[i])
        even(i+1)

x=[12,35,45,68,43,56,78,21,47]
i=0
even(i)

--------------------------------------------------------------

#2)python program to determine how many times a given letter occurs in a
#string recursively

def letter(i,x,ch):
    global cnt
    if i<len(x):
        if ch in x:
            cnt=cnt+1
            print(cnt)
        letter(i+1,x,ch)
    

            
x="aaaaa"
ch=input("enter a letter : ")
i=0
cnt=0
letter(i,x,ch)

-------------------------------------------------------------
#4)python program to find the sum of elements in a list recursively


def SumOfElements():
    global total
    global i
    while i<len(x):
        total=total+x[i]
        i=i+1
        SumOfElements()

i=0
total=0
x=[100,50,20,30,50,300,500,40,60]
SumOfElements()
print(total)

----------------------------------------------------------

#3)python program to find the Fibonacci series using recursion
def Fibonacci(next,prev):
    
    if next<=n:
        print(next)
        temp=next
        next=next+prev
        prev=temp
        Fibonacci(next,prev)

n=int(input("enter a number : "))
a=0
b=1
print(a)
print(b)
Fibonacci(a+b,b)
-------------------------------------------------------


#5)write a python program how many times given letter occurs in a string
# recursively

def CountChar():
    global cnt
    global i
    if i<len(x):
        if ch==x[i]:
            cnt=cnt+1
        i=i+1
        CountChar()

i=0
cnt=0
x=input("enter a string : ")
ch=input("enter a character : ")
CountChar()
print(cnt)

----------------------------------------------------

#6)python program to find the binary equivalent of a number recursively

def binary():
    global i
    if i<10:
        y=bin(i)
        print(y)
        i=i+1
        binary()
    

i=1
binary()
#print(y)

---------------------------------------------------------
'''

#7)python program to find the LCM of two numbers using recursion


x=int(input("enter a number 1 : "))
y=int(input("enter a number 2 : "))
if x>y:
    greater=x
    if greater%x==0 and greater%y==0:
        print("lcm of x,y is : ",x)
else:
    greater=y
    if greater%x==0 and greater%y==0:
        print("lcm of x,y is : ",y)






























