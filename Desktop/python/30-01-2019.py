'''
# python program to run the second largest number in a list
n=int(input("enter no of elements : "))
x=[]
for i in range(1,n+1):
    a=int(input("enter element : "))
    x.append(a)
x=sorted(list(set(x)))
print("secont largest number is",x[-2])


#python program to merge two lists and sort it

x=[1,4,7,2,9,5]
y=[12,54,25,78,90]
z=sorted(x)+sorted(y)
print(z)



#python program to sort a list according to the length of the elements
n=int(input("enter no. of elements : "))
x=[]
for i in range(1,n+1):
    a=input("enter element : ")
    x.append(a)
    
#x=['python','django','aws','unix','linux']
y=[len(i) for i in x]
y.sort()
#print(x)
#print(y)

for i in y:
    for j in x[:]:
        if i==len(j):
            print(j,end=" ")
            x.remove(j)



#python program to find unoin of two lists

x=[1,2,3,5,6]
y=[7,8,9,10]
x=set(x)
y=set(y)
c=x|y
print(c)



#python program to find intersection of two lists


x=[1,2,3,5,6]
y=[5,6,7,8,9,10]
x=set(x)
y=set(y)
c=x&y
print(c)



#python program to create a list of tuples with the first element as the number
#and second element as the square of its number


y=[(i,i*i) for i in list(range(1,51))]
print(y)
'''

#python program to find all numbers in a range which are perfect squares
#and sum of all digits in the number is less than 10

x=int(input("enter any number : "))
for i in range(1,51):
    n=i*i
    if n==x:
        print(x,"perfect square")    
        sum=0
        for j in str((n)):
            sum=sum+int(j)
        if sum<=10:
            print(sum)
        else:
            print("sum is greater than 10",sum)
else:
    print(x,"not a perfect square")

    (or)

x=[]
for i in range(1,1000):
    sqt=i**0.5
    sqr=int(sqt)*int(sqt)
    if i==sqr:
        x.append(i)
print(x)
for i in x:
    tot=0
    for j in str(i):
        tot=tot+int(j)
    if tot<10:
        print(i,end=" ")
        
            
    
    
    




    






























