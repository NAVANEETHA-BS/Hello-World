# print even numbers from 1 to n with comma separator and their sum also

n=int(input("enter a number : "))
sum=0
for i in range(1,n+1):
    if i%2==0:
        print(i, end=",")
        sum+=i
print("\n sum=",sum)

'''
for i in range(2,n+1,2):
    print(i,end=",")
    sum=sum+i
    print("\n 1+2+3+4+5+.....%d,%(n,%d))
    
