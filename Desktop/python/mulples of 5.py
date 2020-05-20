#multiple of 5

n=int(input("enter a number : "))
sum=0
for i in range(1,n+1):
    if i%5==0:
        print(i, end=",")
        sum+=i
print("\n sum=",sum)

