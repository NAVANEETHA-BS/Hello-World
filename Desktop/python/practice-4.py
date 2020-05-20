'''
class Product:
    def __init__(self,price):
        self.price=price
    def __add__(self,x):
        return self.price+x.price
    def __gt__(self,x):
        if self.price>x.price:
            print("product1 more than product2")
        else:
            print("product1 less than product2")
p1=Product(500)
p2=Product(200)
print(p1+p2)
p1.__gt__(p2)
-----------------------------------------
class Product:
    def __init__(self,price):
        self.price=price
    def __add__(self,x):
        return self.price+x.price
    def __gt__(self,x):
        if self.price>x.price:
            print("product1 more than product2")
        else:
            print("product1 less than product2")
p1=Product(500)
p2=Product(100)
print(p1+p2)
p1.__gt__(p2)
---------------------------------------------

class Product:
    def __init__(self,price):
        self.price=price
    def __add__(self,x):
        return self.price+x.price
    def __gt__(self,x):
        if self.price>x.price:
            print("product1 more than product2")
        else:
            print("product1 less than product2")
p1=Product(500)
p2=Product(100)
print(p1+p2)
p1.__gt__(p2)
----------------------------------------------

class Product:
    def __init__(self,price):
        self.price=price
    def __add__(self,x):
        return self.price+x.price
    def __gt__(self,x):
        if self.price>x.price:
            print("product1 more than product2")
        else:
            print("product1 less than product2")
p1=Product(500)
p2=Product(100)
print(p1+p2)
p1.__gt__(p2)
-----------------------------------------------

class Product:
    def __init__(self,price):
        self.price=price
    def __add__(self,x):
        return self.price+x.price
    def __gt__(self,x):
        if self.price>x.price:
            print("product1 more than product2")
        else:
            print("product1 less than product2")
p1=Product(400)
p2=Product(100)
print(p1+p2)
p1.__gt__(p2)
--------------------------------------------

class Product:
    def __init__(self,price):
        self.price=price
    def __add__(self,x):
        return self.price+x.price
    def __gt__(self,x):
        if self.price>x.price:
            print("product1 more than product2")
        else:
            print("product1 less than product2")
p1=Product(500)
p2=Product(100)
print(p1+p2)
p1.__gt__(p2)
----------------------------------------------------

class Product:
    def __init__(self,price):
        self.price=price
    def __add__(self,x):
        return self.price+x.price
    def __gt__(self,x):
        if self.price>x.price:
            print("product1 more than product2")
        else:
            print("product1 less than product2")

p1=Product(400)
p2=Product(100)
print(p1+p2)
p1.__gt__(p2)
-----------------------------------------------------

# Reading data from csv file

import csv

x=open("student.csv","r")
a=csv.reader(x) # It returns csv reader object
print(a,type(a))
for  i  in  a :
    print(i)

x.close()

-------------------------------------------------

# Writing data to csv file

import csv
with  open("student.csv","w",newline='') as x:
    a=csv.writer(x) # It returns csv writer object
    a.writerow(["Sid","Sname","Cname","Fee"])
    n=int(input("Enter no.of students : "))
    for  i   in   range(n) :
        sid=int(input("Enter student id : "))
        sname=input("Enter student name : ")
        cname=input("Enter student course : ")
        fee=float(input("Enter fee : "))
        a.writerow([sid,sname,cname,fee])
print("Inserted sucessfully into file")
-----------------------------------------------------

import csv
x=open("student.csv","r")
a=csv.reader(x)
print(a,type(a))
for i in a:
    print(i)
x.close()
-----------------------------------------------------------
#python 3.0
x={'a':1,'b':2}
y={'b':3,'c':4}
z={**x,**y}
print(z)
--------------------------------------------------------

#python  2.7
x={'a':1,'b':2}
y={'b':3,'c':4}
z=dict(x,**y)
print(z)
------------------------------------------------------

#python code snippet to remove duplicates in a string
import itertools
text="NEEXXxTTGGEENNNCCOODEERR"
text_list=list(text)
new_text=[k for k,g in itertools.groupby(text_list)]
print("".join(new_text))
---------------------------------------------------------

from datetime import date
import calendar

my_date=date.today()
print(calendar.day_name[my_date.weekday()])
------------------------------------------------------------

#how to right align a string with format method
string="HELLO WORLD"

print("{:>15}".format(string))
print("{:>20}".format(string))
---------------------------------------------------------

# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2019
mm = 3

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))
--------------------------------------------------------

import time
seconds=time.time()
print("time is : ",seconds)
-----------------------------------------------------------

import time
print("this prints immediately ....")
time.sleep(5)
print("this prints after 5 seconds")
-----------------------------------------------------------

import time

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

local_time = time.mktime(t)
print("Local time:", local_time)
---------------------------------------------------------


import time

result = time.gmtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
------------------------------------------------------


import time

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)
-------------------------------------------------------

def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()
-----------------------------------------------------------

def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner : ",x)
    inner()
    print("outer : ",x)
outer()
------------------------------------------------------------------

def outer():
    x="local"
    def inner():
        #nonlocal x
        x="nonlocal"
        print("inner : ",x)
    inner()
    print("outer : ",x)
outer()
-------------------------------------------------------------------

def outer():
    x="local"
    def inner():
        nonlocal x
        x="nonlocal"
        print("inner : ",x)
    inner()
    print("outer : ",x)
outer()
-----------------------------------------------------------------

def outer():
    x="local"
    def inner():
        nonlocal x
        x="nonlocal"
        print("inner : ",x)
    inner()
    print("outer : ",x)
outer()
-------------------------------------------------------------


class MyNewClass:
    This is a docstring. I have created a new class
    pass
---------------------------------------------------------------

class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)
------------------------------------------------------------------

class Myclass:
    "This is my second class"
    a = 10
    def func(self):
        print('Hello')
print(Myclass.a)
print(Myclass.func)
print(Myclass.__doc__)
------------------------------------------------------

class Myclass:
    "This is my second class"
    a = 10
    def func(self):
        print("Hello")
print(Myclass.a)
print(Myclass.func)
print(Myclass.__doc__)
---------------------------------------------------

class Myclass:
    "This is my second class"
    a = 10
    def func(self):
        print("Hello")
print(Myclass.a)
print(Myclass.func)
print(Myclass.__doc__)
------------------------------------------------------

class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# create a new MyClass
ob = MyClass()

# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello
ob.func()
---------------------------------------------------------

class Myclass:
    "This is my second class"
    a = 10
    def func(self):
        print("Hello")
ob = Myclass()

print(Myclass.func)
print(ob.func)
ob.func
-----------------------------------------------------------

class Myclass:
    "This is my second class"
    a = 10
    def func(self):
        print("Helllo")
ob = Myclass()

print(Myclass.func)
print(ob.func)
ob.func()
-----------------------------------------------------
'''
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


x=MyClass()
x.i
x.f





































































































































































































































