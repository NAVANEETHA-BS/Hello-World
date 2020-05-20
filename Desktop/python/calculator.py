# calculator

print(" Main Menu ")
print("=============")
print("1. Addition")
print("2. Subtraction")
print("3. Product")
print("4. Division")
print("5. Power")
print("exit")

print("Enter option [1-6]) :")
ans=int(input())
if ans==6:
    print("thank you")
    sys.exit()
elif ans not in(1,2,3,4,5,6):
    print("enter choice between 1 and 6 only")
else:
    a=int(input("enter number 1 :"))
    b=int(input("enter number 2 :"))
    if ans==1:
        c=a+b
        print("sum=",c)
    elif ans==2:
        c=a-b
        print("difference=",c)
    elif ans==3:
        c=a*b
        print("product=",c)
    elif ans==4:
        c=a/b
        print("division=",c)
    elif ans==5:
        c=a**b
        print("power :",c)
                
