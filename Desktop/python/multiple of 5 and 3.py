# multiples of 5 and 3

n=int(input("enter a number : "))
sum=0
for i in range(1,n+1):
    if i%5==0 and i%3==0:
        print(i, end=",")
        sum+=i
print("\n sum=",sum)
