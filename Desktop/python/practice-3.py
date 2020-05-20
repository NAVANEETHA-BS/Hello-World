'''(buffer)
import time
def decrement(n):
    print("counting down,......")
    while(n>0):
        yield n
        n=n-1
x=decrement(5)

for i in x:
    print(i)


import random,time
names=['Ganesh','Hari','Sai','Siva','Lakshmi']
courses=['python','Django','Unix','sql','UI']

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


t1=time.clock()
studs=display_enquiries(10000000)
t2=time.clock()
print("Elapsed time :",t2-t1)

t1=time.clock()
studs=generator_enquiries(10000000)
t2=time.clock()
print("Elapsed time :",t2-t1)
-------------------------------
    
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for i in fib():
    if i>100:
        break
    print(i)


---------------------------------
a=[10,20,30,40,50]
b=iter(a)
while True:
    try:
        print(next(b))
    except StopIteration:
        break


x=[1,2,3,45,3,5,75]
y=iter(x)
while True:
    print(next(y))
    
---------------------------------
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
----------------------------------------------
class Company:
    cname="Tecnosoft"  #class variables/static variables
    phno="9966422225"
    addr="Ameerpet,Hyderabad"

    def __init__(self,empno,ename,job,sal):#constructor method
        self.empno=empno
        self.ename=ename
        self.job=job
        self.sal=sal
    def DisplayEmpDetails(self): #instance method
        print(self.__dict__)
    @classmethod
    def CompanyDetails(cls): #class method
        print("Company Name : {},Phno:{},Addr:{}".format(Company.cname,Company.phno,Company.addr))
    @staticmethod
    def bonus():
        print("this year no bonus")

x=Company(1,'Ganesh','President',90000)
y=Company(2,'Hari','Analyst',85000)
x.DisplayEmpDetails()
y.DisplayEmpDetails()
Company.CompanyDetails()
Company.bonus()
--------------------------------------------------
class Company:
    cname="Tecnosoft" #class variables/static variables
    phno="9966422225"
    addr="Ameerpet,Hyderabad"

    def __init__(self,empno,ename,job,sal): #constructor method
        self.empno=empno
        self.ename=ename
        self.job=job
        self.sal=sal
    def DisplayEmpDetails(self): #instance method
        print(self.__dict__)
    @classmethod
    def CompanyDetails(cls): #class method
        print("Company Name : {},phno :{},Addr :{}".format(Company.cname,Company.phno,Company.addr))
    @staticmethod
    def bonus():
        print("this year no bonus")

x=Company(1,'Ganesh','President',90000)
y=Company(2,'Hari','Analyst',85000)
x.DisplayEmpDetails()
y.DisplayEmpDetails()
Company.CompanyDetails()
Company.bonus()
-------------------------------------------
class Company:
    cname="Tecnosoft" #class variables/static variables
    phno="9966422225"
    addr="Ameerpet,Hyderabad"

    def __init__(self,empno,ename,job,sal):
        self.empno=empno
        self.ename=ename
        self.job=job
        self.sal=sal
    def DisplayEmpDetails(self):
        print(self.__dict__)
    @classmethod
    def CompanyDetails(cls): #class method
        print("company name :{},phno:{},addr:{}".format(Company.cname,Company.phno,Company.addr))
    @staticmethod
    def bonus():
        print("this year no bonus")

x=Company(1,'Ganesh','President',90000)
y=Company(2,"Hari",'Analyst',85000)
x.DisplayEmpDetails()
y.DisplayEmpDetails()
Company.CompanyDetails()
Company.bonus()
-----------------------------------------
class Company:
    cname="Tecnosoft" #class variables/static variables
    phno="9966422225"
    addr="Ameerpet,Hyderabad"

    def __init__(self,empno,ename,job,sal):
        self.empno=empno
        self.ename=ename
        self.job=job
        self.sal=sal
    def DisplayEmpDetails(self):
        print(self.__init__)
    @classmethod
    def CompanyDetails(cls): #class method
        print("Company name:{},phno:{},addr:{}".format(Company.cname,Company.phno,Company.addr))
    @staticmethod
    def bonus():
        print("this year no bonus")

x=Company(1,'Ganesh','President',90000)
y=Company(2,'Hari','Analyst',85000)
x.DisplayEmpDetails()
y.DisplayEmpDetails()
Company.CompanyDetails()
Company.bonus()
--------------------------------------
def f1():
    print("iam local f1")
class Sample:
    def f1(self):
        print("i am f1")
    def f2(self):
        print("i am f2")
    def f3(self):
        f1()
        self.f1()
        self.f2()
        print("i am f3")

x=Sample()
x.f3()
-----------------------------------
def f1():
    print("iam local f1")
class Sample:
    def f1(self):
        print(" iam f1")
    def f2(self):
        print("iam f2")
    def f3(self):
        f1()
        self.f1()
        self.f2()
        print("iam f3")
x=Sample()
x.f3()
---------------------------------
class Sample:
    __a=100
    b=200

    def __f1(self):
        print("iam private f1 function")
    def f2(self):
        print("i am public f2,calling private f1")
        self.__f1()
        print("a=",Sample.__a,self.__a)
x=Sample()
x.f2()
print("b=",Sample.b,x.b)
---------------------------------
class Sample:
    __a=100
    b=200
    def __f1(self):
        print("iam private f1 function")
    def f2(self):
        print("iam public f2,calling private f1")
        self.__f1()
        print("a=",Sample.__a,self.__a)
x=Sample()
x.f2()
print("b=",Sample.b,x.b)
---------------------------------
class Sample:
    __a=100
    b=200
    def __f1(self):
        print("iam private f1 method")
    def f2(self):
        print("iam public f2,calling private f1")
        self.__f1()
        print("a=",Sample.__a,self.__a)
x=Sample()
x.f2()
print("b=",Sample.b,x.b)
---------------------------------------

class Sample:
    __a=100
    b=200
    def __f1(self):
        print("iam private f1 method")
    def f2(self):
        print("iam public f2,calling private f1")
        self.__f1()
        print("a=",Sample.__a,self.__a)
x=Sample()
x.f2()
print("b=",Sample.b,x.b)
----------------------------------------
import pickle
class Employee:
    def __init__(self,ename,job,sal):
        self.ename=ename
        self.job=job
        self.sal=sal
    def display(self):
        pass
e1=Employee('sai','president',100000)
x=open('emp1.txt','wb')
#pickling process
pickle.dump(e1,x)
x.close()

x=open('emp1.txt','rb')
#unpickling process
y=pickle.load(x)
print(y.ename,y.job,y.sal)
x.close()
'''

import random
names=['Ganesh','Hari','Siva','Lakshmi','Sai','Vishnu']
courses=['Django','Python','SQL','AWS','Devops','Unix']
fee=[10000,5000,9000,12000,15000,6000,8000,20000,11000]
print("%-5s%-15s%-15s%-10s"%("Sid","Sname","Course","Fee"))
for i in range(1,10):
    sid=random.randint(100,1000)
    name=random.choice(names)
    course=random.choice(courses)
    fee=float(random.randrange(5000,20000,10))
    print("%-5d%-15s%-15s%-8.2f"%(sid,name,course,fee))

















































































































































        
























        






























