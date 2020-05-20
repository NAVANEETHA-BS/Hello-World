
#enclosure
#nested function
#here we are returning reference of inner function
'''
def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner
a=outer()
#print(a())
print(a)
--------------------------------

def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner
a=outer()
print(a)
-----------------------------

def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner
a=outer()
print(a)
------------------------------

def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner
a=outer()
print(a)
---------------------------------

def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner
a=outer()
print(a)
-------------------------------------

def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner
a=outer()
print(a)
----------------------------------------
-----------------------------------------------
def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner
a=outer()
print(a)
--------------------------------------------

def outer():
    x=3
    def inner():
        y=4
        result=x+y
        return result
    return inner
a=outer()
print(a)
--------------------------------------------

def outer():
    x=3
    def inner():
        y=4
        result=x+y
        return result
    return inner
a=outer()
print(a.__name__)
------------------------------------------------

#function as parameter to another function

def function1():
    print("hi i am function1")

def function2(func):
    print("hi i am function 2 now i will call function1")
    func()

function2(function1)
-------------------------------------------------
'''
#function as parameter to another function
'''
def function1():
    print("hi i am function1")

def function2(func):
    print("hi i am function2 now i will call function1")
    func()
function2(function1)
'''
#function as parameter to another function
'''
def function1():
    print("hi i am function1")

def function2(func):
    print("hi i am function2 now i will call function1")
    func()
function2(function1)
'''
#function as parameter to another function
'''
def function1():
    print("hi i am function1")

def function2(func):
    print("hi i am function2 now i will call function1")
    func()
function2(function1)
'''
#decorator

#1)multiple decorator
#2)decorator parameter
#3)multiple function

#1)multiple decorator
'''
def upper_d(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner

def split_d(func):
    def wrapper():
        str2=func()
        return str2.split()
    return wrapper

@split_d
@upper_d
def ordinary():
    return "good morning"
print(ordinary())
'''
#1)multiple decorator
'''
def upper_d(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner

def split_d(func):
    def wrapper():
        str2=func()
        return str2.split()
    return wrapper

@split_d
@upper_d
def ordinary():
    return "good morning"
print(ordinary())
'''
#1)multiple decorator
'''
def upper_d(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner

def split_d(func):
    def wrapper():
        str2=func()
        return str2.split()
    return wrapper

@split_d
@upper_d
def ordinary():
    return "good morning"
print(ordinary())
'''
#1)multiple decorator
'''
def upper_d(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner

def split_d(func):
    def wrapper():
        str2=func()
        return str2.split()
    return wrapper

@split_d
@upper_d
def ordinary():
    return "good morning"
print(ordinary())
'''

'''
def outer(expr):
    def upper_d(func):
        def inner():
            return func() + expr
        return inner
    return upper_d

@outer(" amulya")
def ordinary():
    return "good morning"

print(ordinary())
'''
'''
def outer(expr):
    def upper_d(func):
        def inner():
            return func() + expr
        return inner
    return upper_d

@outer(" amulya")
def ordinary():
    return "good morning"

print(ordinary())
'''

#multiple function decorators

def div_decorator(func):
    def inner(*args):
        list1=[]
        list1=args[1:]
        for i in list1:
            if i==0:
                return "give proper input!!!"
        return func(*args)
    return inner

@div_decorator
def div1(a,b):
    return a/b

@div_decorator
def div2(a,b,c):
    return a/b/c

print(div1(1,2))
print(div2(1,9,10))







            






































































    























































    


























































































































