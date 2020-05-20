# count number of even numbers and odd numbers

n=input("enter a number : ")

even_cnt=0
odd_cnt=0

for i in n:
    if int(i)!=0:
        if int(i)%2==0:
            even_cnt+=1
        else:
            odd_cnt+=1
print("number of even numbers in a %s is : %d" %(n,even_cnt))
print("number of odd numbers in a %s is : %d" %(n,odd_cnt))
if even_cnt>odd_cnt:
    print("even numbers more than odd numbers in a %s number " %(n))
elif even_cnt<odd_cnt:
    print("odd numbers more than even numbers in a %s number " %(n))
else:
    print("both are equal")
