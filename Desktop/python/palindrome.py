#accept a number check the given number is palindrome or not

n=int(input("enter a number : "))
temp=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10

if temp==rev:
    print(temp,"is a palindrome numbers")
else:
    print(temp,"is not a palindrome numbers")


    '''
n=input("enter a number :")
rev=n[::-1]

if n==rev:
    print(n,"is a palindrome numbers")
else:
    print(n,"is not a palindrome numbers")
            
