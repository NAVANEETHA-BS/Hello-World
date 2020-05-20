'''
17)

        *  
       * *
      * * *
     * * * *
    * * * * *
   * * * * * *
  * * * * * * *
 * * * * * * * *
* * * * * * * * *


n=int(input("enter number of rows : "))
k=(n//2)
for i in range(1,n+1):
    print()
    for j in range(k,0,-1):
        print("",end=" ")
    k=k-1
    for m in range(1,i+1):
        print(" * ",end=" ")
   
    
'''

n=int(input("enter number of rows : "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()


    for l in range(1,i+1):
        print("*",end="")
    print()











