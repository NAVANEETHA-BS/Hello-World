# generator
#it is a function to generate values
#it contains yield statement
#it does not delete memory for local variables
#it increases perfomance
'''
import copy
a=[10,20,30,40,50]
b=copy.copy(a) #shallow copy

print(a,id(a)) #[10,20,30,40,50] 47295224
print(b,id(b)) #[10,20,30,40,50] 47358960
a[2]=222

print(a,id(a)) #[10,20,222,40,50] 47295224
print(b,id(b)) #[10,20,30,40,50] 47358960
'''
#-----------------------------
'''
import copy

a=[[1,2,3],[4,5,6],[7,8,9]]
b=copy.copy(a)
print(a)
print(b)

a.append([10,11,12])
print(a)
print(b)

a[2][2]=2222
print(a)
print(b)
'''
#----------------------------------------
'''
import time
def decrement(n):
    print("counting down,....")
    while(n>0):
        yield n #function having yield keyword called generator
        n=n-1

x=decrement(5)

for i in x:
    print(i)
'''

#---------------------------------------------
'''
x=[i*i for i in range(100000000)]
print(type(x),x[0])

# output: memory error
'''
#------------------------- 
'''
y=(i*i for i in range(100000000000)) #generator
print(type(y),next(y))

'''
#-------------------------
'''
import copy
a=[10,20,[30,40],50]
b=copy.copy(a)  #shallow copy

print(a,id(a)) #[10,20,30,40,50] 47295224
print(b,id(b)) #[10,20,30,40,50] 47358960

a[2][0]=333
print(a,id(a))
print(b,id(b))

print(id(a[1]),id(b[1]))
print(id(a[2]),id(b[2]))

'''
#---------------------------------
'''
import random,time
names=['Ganesh','Hari','Sai','Siva','Lakshmi']
courses=['Python','Django','Unix','Sql','Ui']

def display_enquiries(n):
    enqs=[]
    for i in range(n):
        student={'id':i,'name':random.choice(names),'course':random.choice(courses)}
        enqs.append(student)
    return enqs
def generator_enquiries(n):
    for i in range(n):
        student={'id':i,'name':random.choice(names),'course':random.choice(courses)}
        yield student

#----------
t1=time.clock()
studs=display_enquiries(10000000)
t2=time.clock()
print("Elapsed time :",t2-t1)

#---------
t1=time.clock()
studs=generator_enquiries(10000000)
t2=time.clock()
print("Elapsed time :",t2-t1)
    
'''
#--------------------------------------------
'''
#fibonacci

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for i in fib():
    if i>100:
        break
    print(i)

'''
#--------------------------
'''
a=[10,20,30,40,50]
b=iter(a)
while True:
    try:
        print(next(b))
    except StopIteration :
        break

# (or)--------------------
for i in a :
    print(i)

'''
#------------------------------------

def mygen():
    yield "Hello"
    yield "Python"
    yield "World"

g=mygen()
print(type(g))
print(next(g))
print(g.__next__())
print(next(g))

'''
for i in mygen():
    print(i)
'''






































































































        
