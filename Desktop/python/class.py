#example of instance/class/static methods
'''
class Company:
    cname="Tecnosoft" #class variables/static variables
    phno="9966422225"
    addr="Ameerpet,Hyderabad"

    def __init__(self,empno,ename,job,sal): #constructor method
        self.empno=empno #instance variable/non static variables
        self.ename=ename
        self.job=job
        self.sal=sal
    def DisplayEmpDetails(self): #instance method
        print(self.__dict__)
    @classmethod
    def CompanyDetails(cls): #class method
        print("company name :{},phno:{},addr :{}".format(Company.cname,Company.phno,Company.addr))
    @staticmethod
    def bonus():
        print("this year no bonus")

x=Company(1,'Ganesh','President',90000)
y=Company(2,'Hari','Analyst',85000)
x.DisplayEmpDetails()
y.DisplayEmpDetails()
Company.CompanyDetails()
Company.bonus()

 '''
#example of destructor
'''
class Employee:
    cnt=0
    def __init__(self):
        Employee.cnt+=1
        print("employee joined :",Employee.cnt)
    def __del__(self):
        Employee.cnt-=1
        print("removed employee :",Employee.cnt)

def f1():
    a=Employee()
    b=Employee()

x=Employee()
f1()
y=Employee()
del x
del y
'''

#example of destructor
'''
class Sample:
    def __init__(self):
        print("iam a constructor")
    def __del__(self):
        print("iam a destructor")

def f1():
    a=Sample()
    b=Sample()

x=Sample()
f1()
y=Sample()
del x
del y

'''

#how to call a class function within same class function
'''
def f1():
    print("i an local f1")

class Sample:
    def f1(self):
        print("iam f1")
    def f2(self):
        print("i am f2")
    def f3(self):
        f1() # iam local f1
        self.f1()#iam f1
        self.f2()
        print("i am f3")
x=Sample()
x.f3()
'''
#

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









































































        
        
