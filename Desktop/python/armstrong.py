#accept a number and print given number is armstrong number or not

n=input("enter a number : ")
sum=0
for i in n:
    i=int(i)
    sum=sum+i**3
print(sum)
if sum==int(n):
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")


    
