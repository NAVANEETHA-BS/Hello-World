'''
#python program to generate random numbers from 1 to 20 and
#append them to the list

import random
x=[]

for i in range(1,21):
    y=random.randint(1,20)
    x.append(y)
print(x)

#python program to sort a list of tuples in increasing
#order by the last element in each tuple

x=[(9,7),(2,3),(4,1),(5,6),(3,5)]
y={}
for i in x:
    y=[i[-1]]=i[0]
keys=sorted(y.keys())
print(keys)
a=[]
for i in keys:
a.append(y[i],i])
print(x)
print(a)



#python program to swap the first and last value of a list

x=[1,2,3,4,5]

temp=x[0]
x[0]=x[-1]
x[-1]=temp
print(x)
(or)
x[0],x[-1]=x[-1],x[0]
print(x)



#write a python program to count the number of strings where
#the string length is 2 or more and the first and last character
#are same from a given list of strings
#sample list : ['abc','xyz','aba','1221']
#expected result : 2

x=['a','abc','xyz','aba','1221']
count=0
for i in x:
    if len(i)>=2 and i[0]==i[-1]:
        print(i)
        count=count+1
print(count)

#write a python program that takes two lists and returns True if they have
#atleast one common member

x=[1,2,3,4,5]
y=[4,5,6,7,8]
x=set(x)
y=set(y)
n=x&y
if len(n)>=1:
    print(True)

    (or)

import random
x=[]
y=[]
for i in range(1,10):
    x.append(random.randint(1,10))
    y.append(random.randint(1,10))
print(x)
print(y)

for i in x:
    if i in y:
        print("yes,there are common elements ")
        break
else:
    print("there are no common elements ")

    


#write a python program to print a specified list after removing the 0th,
#4th and 5th elements
#sample list : ['Red','Green','White','Black','Pink','Yellow']
#expected o/p : ['Green','White','Black']

x=['Red','Green','White','Black','Pink','Yellow']
a=x[0]
b=x[4]
c=x[5]

x.remove(a)
x.remove(b)
x.remove(c)

print(x)
    

#write a python program to print the number of a specified
#list after removing even numbers from it

x=[1,2,4,5,6,8,10,12]
for i in x[:]:
    if i%2==0:
        x.remove(i)
print(x)
'''


#write a python program to shuffle and print the specified list
import random
x=[1,2,3,4]
random.shuffle(x)
print(x)













        












        

























