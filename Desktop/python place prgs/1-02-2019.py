'''
# write a python program to generate and print a list of first and
#last 5 elements where the values are square of numbers between 1 and 30
#(both included)

import random

x=[]
for i in range(1,31):
    x.append(random.randint(1,1000))
y=x[:5]+x[-5:]
z=[i*i for i in range(1,31)]
for i in y:
    if i in z:
        print(i)
            
#write a python program to generate and print a list except for the first
#5 elements, where the values are square of numbers between 1 and 30
#(both included)

import random
x=[]
for i in range(1,31):
    x.append(random.randint(1,1000))
y=x[5:]
print(y)
z=[i*i for i in range(1,31)]
for i in y:
    if i in z:
        print(i)


#write a python program to get the difference between the two lists
import random
x=[]
y=[]
for i in range(1,15):
    x.append(random.randint(1,20))
    y.append(random.randint(1,20))
print(x)
print(y)
n=set(x)
m=set(y)
z=n-m
print(z)


#write a python program to convert a list of characters into string

x=['s','t','r','i','n','g']
for i in x:
        print(i,end="")



#write a python program to select an item randomly from a list
import random
x=['ss','ab','20','25','2a']

y=random.choice(x)
print(y)



#write a python program to get the frequency of the elements in a list

x=[1,2,3,4,2,5,5,3,8,6,9,7,6,8,9]
d={}

for i in x:
    d[i]=x.count(i)
print(d)


#write a python program to check wheather a list contains a sublist

#x=[23,34,[2,3,6],21,76]
x=[1,2,3,4]
for i in x:
    if type(i) is list:
        print("list contains sublist")
        break
else:
    print("list doesn't contains sublist")


#write a python program to create a list by concatenating a given
#list which range goes from 1 to n
#sample list:['p','q']
#n=5
#sample o/p: ['p1','q1','p2','q2','p3','q3','p4','q4','p5','q5']

x=['p','q']
y=[]

for i in list(range(1,5)):
    for j in x:
       # print((j+str(i)),end=",")
        z=(j+str(i))
        y.append(z)
print(y)



#write a python program to convert a list of multiple integers into a single
#integer
#sample list: [11,33,50]
#expected o/p: 113350

#import random
x=[]
for i in range(1,10):
    x.append(i)
print(x)
for i in x:
    print(i,end="")

'''

#write a python program to split a list based on the first character of word

x=['apple','banana','orange','grapes']
for i in x:
#x=set(x)
#print(i[0],end=" ")
    y=i.split("i[0]")
    print(y)








































              
    
    
    
    








    
    




    
    

























