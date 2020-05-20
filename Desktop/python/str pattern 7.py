'''
7)tecno

    t
   et
  cet
 ncet
oncet
'''

x=input("enter a string : ")
l=len(x)
for i in range(0,l):
    print(" "*(l-i+1),end="")
    print(x[i::-1])

         
