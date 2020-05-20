'''
d1={'what is national fruit?':['Apple','Banana','Mango','chickoo'],
    'what is national flower?':['Rose','Lotus','Sun flower','Jasmine'],
    'what is national animal?':['Giraffe','Lion','Elephant','Tiger'],
    'what is national Sport?':['Cricket','Hockey','Tennis','Kabadi'],
    'what is national Bird?':['Peacock','Parrot','Kivi','Crane']}

key=(3,2,4,2,1)
index=0
score=0
for i,j in d1.items():
    print(i)
    for n,m in enumerate(j):
        print(n+1,".",m)
    ans=int(input("enter an option : "))
    if ans==key[index]:
        score+=1
    index+=1
print("your score is : ",score)
---------------------------------------------------------------------

d1={'what is national fruit?':['Apple','Banana','Mango','Chickoo'],
    'what is national flower?':['Rose','Lotus','Sun flower','Jasmine'],
    'what is national animal?':['Giraffe','Lion','Elephant','Tiger'],
    'what is national sport?':['Cricket','Hockey','Tennis','Kabadi'],
    'what is national bird?':['peacock','parrot','kivi','crane']}
key=[3,2,4,2,1]
index=0
score=0
for i,j in d1.items():
    print(i)
    for n,m in enumerate(j):
        print(n+1,".",m)
    ans=int(input("enter option :"))
    if ans==key[index]:
        score+=1
    index+=1
print("your score is :",score)
----------------------------------------------------------------------

d1={'what is national fruit?':['Apple','Banana','Mango','Chickoo'],
    'what is national flower?':['Rose','Lotus','sunflower','Jasmine'],
    'what is national animal':['giraffe','lion','elephant','tiger'],
    'what is national sport':['cricket','hockey','tennis','kabadi'],
    'what is national bird':['peacock','parrot','kivi','crane']}
key=[3,2,4,2,1]
index=0
score=0
for i,j in d1.items():
    print(i)
    for n,m in enumerate(j):
        print(n+1,".",m)
    ans=int(input("enter option : "))
    if ans==key[index]:
        score+=1
    index+=1
print("your score is :",score)
----------------------------------------------------------

d1={'what is national fruit?':['Apple','Banana','Mango','Chickoo'],
    'what is national flower?':['Rose','Lotus','sunflower','jasmine'],
    'what is national animal?':['giraffe','lion','sunflower','tiger'],
    'what is national sport?':['cricket','hockey','tennis','kabadi'],
    'what is national bird?':['peacock','parrot','kivi','crane']}
key=[3,2,4,2,1]
index=0
score=0
for i,j in d1.items():
    print(i)
    for n,m in enumerate(j):
        print(n+1,".",m)
    ans=int(input("enter option : "))
    if ans==key[index]:
        score+=1
    index+=1
print("your score is : ",score)
--------------------------------------------------------

def f1(instanceof,a):
    if instanceof=="int":
        print("iam integer")
    elif instanceof==list:
        print("iam list")
    elif instanceof=="str":
        print("iam string")
f1("int",100)
f1('list',[10,20,30])
f1('str','tecnosoft')
----------------------------------------------------

def f1(a):
    print("iam integer")
def f1(b):
    print("iam list")
def f1(c):
    print("iam string")

f1([100,200])
f1('string')
f1(10)

-----------------------------------------

import sys
x=open(sys.argv[1],'r')
data=x.readlines()
print("total no of records : ",len(data))
x.close
-------------------------------------------------

class Sample:
    def f1(self):
        print("iam f1",self)
x=Sample()
y=Sample()
z=Sample()

x.f1()
y.f1()
z.f1()
--------------------------------------------------

class Sample():
    def f1(self):
        print("Iam f1")
x=Sample()
y=Sample()
z=Sample()

x.f1()
y.f1()
z.f1()
--------------------------------------------------

class Student:
    def getdata(self,name,a,b):
        self.name=name
        self.tmarks=a
        self.pmarks=b
    def total_marks(self):
        self.tot_marks=self.tmarks+self.pmarks
    def result(self):
        print(self.name,",",self.tmarks,",",self.pmarks,",",self.tot_marks)
x=Student()
y=Student()
z=Student()

x.getdata("hari",10,20)
y.getdata("neetu",11,21)
z.getdata("geetha",12,22)
print("student name,theory marks,practical marks,total marks")

x.total_marks()
y.total_marks()
z.total_marks()

x.result()
y.result()
z.result()
--------------------------------------------------------
'''
class Student:
    def getdata(self,name,a,b):
        self.name=name

        self.tmarks=a
        self.pmarks=b
    def total_marks(self):
        self.tot_marks=self.tmarks+self.pmarks
    def result(self):
        print(self.name,",",self.tmarks,",",self.pmarks,",",self.tot_marks)
x=Student()
y=Student()
z=Student()
x.getdata("rani",10,20)
y.getdata("neet",11,21)
z.getdata("geet",12,22)
print("name,theory marks,practical marks,total marks")
x.total_marks()
y.total_marks()
z.total_marks()
x.result()
y.result()
z.result()















        
































































































