'''
16)

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
n=int(input("enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for k in range(n-1,0,-1):
    for l in range(1,k+1):
        print(l,end=" ")
    print()
