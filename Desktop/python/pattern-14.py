'''
14)

5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''

n=int(input("enter number of rows : "))
for i in range(n,0,-1):
    for j in range(n,n-i,-1):
        print(j,end=" ")
    print()
