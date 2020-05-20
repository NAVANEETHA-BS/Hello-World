'''
#check digit or not


n=input("enter a digit :")
if len(n)==1:
   if n in "0123456789":
       print("given  number is a digit")
   else:
      print("given number is not a digit")
else:
    print("pz enter only one digit")

    '''
#positive or negative
x=int(input("enter a number : "))
if x>0:
   print(x,"positive number")
elif x<0:
   print(x,"negative number")
else:
   print(x,"neither positive nor negative number")
      
