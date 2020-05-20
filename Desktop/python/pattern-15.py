'''
15)

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

n=int(input("enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
        
for k in range(n-1,0,-1):
    for l in range(1,k):
        print("*",end=" ")
    print()
