#print all palindrome numbers from 1 to 1000

for i in range(1,1001):
    temp=i
    rev=0
    while i>0:
        r=i%10
        rev=rev*10+r
        i=i//10

    if temp==rev:
        print(temp,"palindrome number")
    else:
        print(temp,"not a palindrome number")
    
        
        
    
