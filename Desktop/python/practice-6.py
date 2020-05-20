'''
def   wish(name) :
    print("Hello",name,"good morning,Have a nice day!")

x=wish('Sai') # function calling
print(x,type(x)) # None NoneType

a=wish
a('Hari') # here, we are calling wish function with its alias name
print(a,type(a))
-------------------------------------------------------

def wish(name):
    print("Hello",name,"good morning, Have a nice day!")

x=wish('sai')
print(x,type(x))

a=wish
a('Hari')
print(a,type(a))
-------------------------------------------------------

def wish(name):
    print("Hello",name,"good morning, Have a nice day!")

x=wish('sai')
print(x,type(x))

a=wish
a('Hari')
print(a,type(a))
---------------------------------------------------

def wish(name):
    print("Hello",name,"good morning, Have a nice day!")

x=wish('sai')
print(x,type(x))

a=wish
a('Hari')
print(a,type(a))
-----------------------------------------------------

def wish(name):
    print("Hello",name,"good morning, Have a nice day!")

x=wish('sai')
print(x,type(x))

a=wish
a('Hari')
print(a,type(a))
---------------------------------------------------

def wish(name):
    print("Hello",name,"good morning, Have a nice day!")

x=wish('sai')
print(x,type(x))

a=wish
a('Hari')
print(x,type(x))
--------------------------------------------------------

def wish(name):
    print("Hello",name,"good morning, Have a nice day!")

x=wish('sai')
print(x,type(x))

a=wish
a('Hari')
print(x,type(x))
----------------------------------------------------

def wish(name):
    print("Hello",name,"good morning, Have a nice day!")

x=wish('sai')
print(x,type(x))

a=wish
a('Hari')
print(x,type(x))
------------------------------------------------------

def wish(name):
    print("Hello",name,"good morning, Have a nice day!")

x=wish('sai')
print(x,type(x))

a=wish
a('Hari')
print(x,type(x))
------------------------------------------------------

def wish(name):
    print("Hello",name,"good morning, Have a nice day!")

x=wish('sai')
print(x,type(x))

a=wish
a('Hari')
print(x,type(x))
----------------------------------------------------

def   outer() :
    print("Outer function running,...")
    def  inner() :
        print("Executing inner function")
    print("and outer funtion returning inner function")
    return inner

f1=outer()
f1()
f1()
inner()
---------------------------------------------------

def outer():
    print("outer function running,....")
    def inner():
        print("Executing inner function")
    print("and outer function returning inner function")
    return inner

f1=outer()
f1()
f1()
inner()
-----------------------------------------------------

import pandas as pd
x=pd.Series()
print(x)
--------------------------------------------------

import pandas as pd
data=['a','b','c','d']
x=pd.Series(data)
print(x)
-----------------------------------------------------

import pandas as pd
data=('a','b','c','d')
x=pd.Series(data)
print(x)
--------------------------------------------------------

import pandas as pd
import numpy as np
data=['a','b','c','d']
x=np.array(data)
y=pd.Series(x)
print(y)
---------------------------------------------------------

import pandas as pd
import numpy as np
data=['a','b','c','d']
x=np.array(data)
y=pd.Series(x,index=[101,102,103,104])
print(y)
--------------------------------------------------------

import pandas as pd
data={'a':0.,'b':1.,'c':2.,'d':3.}
x=pd.Series(data)
print(x)
--------------------------------------------------------

import pandas as pd
import numpy as np
data={'a':0.,'b':1.,'c':2.}
x=pd.Series(data,index=['b','d','c','a'])
print(x)
---------------------------------------------------

import pandas as pd
import numpy as np
x=pd.Series(5,index=[1,2,3,4,5])
print(x)
---------------------------------------------------

import pandas as pd
import numpy as np
x=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(x)
print(x[0])
-----------------------------------------------------

import pandas as pd
x=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(x[:3])
print(x[-3:])
---------------------------------------------------

import pandas as pd
x=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(x['b'])
------------------------------------------------------

import pandas as pd
x=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(x[['a','b','e']])
-------------------------------------------------------

import pandas as pd
df=pd.DataFrame()
print(df)
------------------------------------------------------

import pandas as pd
data=[1,2,3,4,5]
df=pd.DataFrame(data)
print(df)
-----------------------------------------------------

import pandas as pd
data=[['neetha',28],['geetha',18]]
df=pd.DataFrame(data,columns=['Name','age'])
print(df)
---------------------------------------------------------

import pandas as pd
data=[['neetha',20],['geetha',15]]
df=pd.DataFrame(data,columns=['Name','age'],dtype='float')
print(df)
-------------------------------------------------------------

import pandas as pd
data={'name':['neetha','geetha','rita'],'age':[15,16,18]}
df=pd.DataFrame(data)
print(df)
-----------------------------------------------------------

import pandas as pd
data={'name':['neetha','geetha','rita','deepa'],'age':[17,10,32,23]}
df=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
print(df)
-------------------------------------------------------

import pandas as pd
data=[{'a':1,'b':2},{'a':3,'b':4,'c':5}]
df=pd.DataFrame(data)
print(df)
----------------------------------------------------------

import pandas as pd
data=[{'a':1,'b':2,'c':3},{'a':4,'b':5,'c':6}]
df=pd.DataFrame(data,index=['rank1','rank2'])
print(df)
-------------------------------------------------------

import pandas as pd
data=[{'a':1,'b':2,'c':3},{'a':4,'b':5,'c':6}]
df1=pd.DataFrame(data,index=['name1','name2'],columns=['a','b'])
df2=pd.DataFrame(data,index=['name1','name2'],columns=['a1','b1'])
print(df1)
print(df2)
------------------------------------------------------------

import pandas as pd
data={'one':pd.Series([1,2,3],index=['a','b','c']),
      'two':pd.Series([5,6,7,8],index=['a','b','c','d'])}
df=pd.DataFrame(data)
print(df)
---------------------------------------------------------------

import pandas as pd
data={'one':pd.Series([1,2,3],index=['a','b','c']),
      'two':pd.Series([4,5,6,7],index=['a','b','c','d'])}
df=pd.DataFrame(data)
print(df['one'])
-------------------------------------------------------------

import pandas as pd
data={'one':pd.Series([1,2,3],index=['a','b','c']),
      'two':pd.Series([4,5,6,7],index=['a','b','c','d'])}
df=pd.DataFrame(data)
print(df)
df['three']=pd.Series([5,6,7],index=['a','b','c'])
print(df)

df['four']=df['one']+df['three']
print(df)

df['five']=df['one']+df['two']
print(df)
--------------------------------------------------------------

import pandas as pd
data={'one':pd.Series([1,2,3],index=['a','b','c']),
      'two':pd.Series([4,5,6,7],index=['a','b','c','d']),
      'three':pd.Series([5,6,7,8],index=['a','b','c','d'])}
df=pd.DataFrame(data)
print(df)

del df['three']
print(df)

df.pop('two')
print(df)
-----------------------------------------------------------

import pandas as pd
data={'one':pd.Series([1,2,3],index=['a','b','c']),
      'two':pd.Series([4,5,6,7],index=['a','b','c','d']),
      'three':pd.Series([5,6,7,8],index=['a','b','c','d'])}
df=pd.DataFrame(data)
print(df)


x=df.loc['b']
print(x)

y=df.iloc[1]
print(y)

print(df[1:2])
----------------------------------------------------------

import pandas as pd
df=pd.DataFrame([[1,2,3],[4,5,6]],columns=['a','b','c'])
df1=pd.DataFrame([[10,11,12],[13,14,15]],columns=['a','b','c'])

x=df.append(df1)
print(x)

df=df.drop(0)
print(df)
------------------------------------------------------------

import pandas as pd
import numpy as np
data=np.random.rand(2,3,4)
p=pd.Panel(data)
print(p)
-------------------------------------------------------------

import pandas as pd
p=pd.Panel()
print(p)
-----------------------------------------------------------

import pandas as pd
import numpy as np
data={'item1':pd.DataFrame(np.random.randn(4,3)),
      'item2':pd.DataFrame(np.random.randn(4,2))}
p=pd.Panel(data)
print(p['item1'])
print(p['item2'])
------------------------------------------------------

import pandas as pd
import numpy as np
data={'item1':pd.DataFrame(np.random.randn(4,3)),
      'item2':pd.DataFrame(np.random.randn(4,2))}
p=pd.Panel(data)

print(p['item1'])
print(p['item2'])

print(p.major_xs(1))

print(p.minor_xs(1))
--------------------------------------------------------

import pandas as pd
import numpy as np

x=pd.Series(np.random.randn(4))
print(x)
--------------------------------------------------------

import pandas as pd
import numpy as np

x=pd.Series(np.random.randn(4))

print(x.axes)
-----------------------------------------------------

import pandas as pd
import numpy as np

x=pd.Series(np.random.randn(4))

print(x.empty)
------------------------------------------------------

import pandas as pd
import numpy as np

x=pd.Series(np.random.randn(4))

print(x)
print(x.ndim)
------------------------------------------------------

import pandas as pd
import numpy as np

x=pd.Series(np.random.randn(4))

print(x)
print(x.size)
-----------------------------------------------------

import pandas as pd
import numpy as np

x=pd.Series(np.random.randn(4))

print(x)
print(x.values)
----------------------------------------------------

import pandas as pd
import numpy as np

x=pd.Series(np.random.randn(4))

print(x)

print(x.head(2))

print(x.tail(2))
------------------------------------------------------

import pandas as pd
import numpy as np

data={'name':pd.Series(['neetha','geetha','rita','tina','ritu']),
      'age':pd.Series([16,46,44,34,33]),
      'rating':pd.Series([2.12,2.11,3.44,3.55,3,54])}
x=pd.DataFrame(data)
print(x)

print(x.T)
----------------------------------------------------------

import pandas as pd
import numpy as np

data={'name':pd.Series(['neetha','geetha','rita','deepu','ritu']),
      'age':pd.Series([23,44,44,33,22]),
      'ranking':pd.Series([2.33,3.34,2.56,6.44,6.32])}

d=pd.DataFrame(data)
print(d)
print(d.size)
----------------------------------------------------------------

import pandas as pd
import numpy as np

data={'name':pd.Series(['neetha','deepa','geetha','ritu','neetu']),
      'age':pd.Series([23,54,55,33,23]),
      'ranking':pd.Series([2.12,2.34,3.55,5.33,3.55])}
x=pd.DataFrame(data)
print(x)

print(x.shape)
-------------------------------------------------------------

import pandas as pd
import numpy as np

data={'name':pd.Series(['neetha','geetha','ritu','deepu','tanu']),
      'age':pd.Series([19,23,22,11,26]),
      'ranking':pd.Series([1.11,2.22,3.33,4.44,5.55])}
d=pd.DataFrame(data)
print(d)
print(d.axes)
-----------------------------------------------------------

import pandas as pd
import numpy as np

data={'name':pd.Series(['neetu','neetha','deepu','deepa','ritu']),
      'age':pd.Series([12,13,14,15,16]),
      'ranking':pd.Series([1.11,2.22,3.33,4.44,5.55])}
d=pd.DataFrame(data)
print(d)
print(d.empty)
----------------------------------------------------------

import pandas as pd
import numpy as np

data={'name':pd.Series(['neetu','neetha','deepu','deepa','ritu']),
      'age':pd.Series([12,13,14,15,16]),
      'ranking':pd.Series([1.11,2.22,3.33,4.44,5.55])}
d=pd.DataFrame(data)
print(d)
print(d.dtypes)
--------------------------------------------------------

import pandas as pd
import numpy as np

data={'name':pd.Series(['neetu','neetha','deepu','deepa','ritu']),
      'age':pd.Series([12,13,14,15,16]),
      'ranking':pd.Series([1.11,2.22,3.33,4.44,5.55])}
d=pd.DataFrame(data)
print(d)
print(d.ndim)
-----------------------------------------------------------

import pandas as pd
import numpy as np

data={'name':pd.Series(['neetu','neetha','deepu','deepa','ritu']),
      'age':pd.Series([12,13,14,15,16]),
      'ranking':pd.Series([1.11,2.22,3.33,4.44,5.55])}
d=pd.DataFrame(data)
print(d)
print(d.values)
-------------------------------------------------------------------

import pandas as pd
import numpy as np

data={'name':pd.Series(['neetha','geetha','rani','meenu','deepa','sravs']),
      'age':pd.Series([21,32,23,11,22,33]),
      'rating':pd.Series([1.11,2.22,3.33,4.44,5.55,6.66])}
y=pd.DataFrame(data)
print(y)
print(y.sum())
print(y.sum(1))

print(y.mean())

print(y.std())

print(y.max())

print(y.describe(include='object'))

print(y.describe(include='all'))

print(y.describe(include='number'))
-------------------------------------------------------------


import pandas as pd
import numpy as np

def adder(e1e1,e1e2):
    return e1e1+e1e2

df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df.pipe(adder,2))
#print(df.apply(np.mean))
----------------------------------------------------------

import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df.apply(np.mean))
-----------------------------------------------------------

import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df.apply(np.mean,axis=1))
--------------------------------------------------------------

import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df['col1'].map(lambda x:x*100))
print(df.apply(np.mean))
--------------------------------------------------------------

import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})

#reindex the DataFrame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])

print (df_reindexed)
-------------------------------------------------------------------

import pandas as pd

url ='https://raw.github.com/pandasdev/pandas/master/pandas/tests/data/tips.csv'

tips=pd.read_csv(url)
print (tips.groupby('sex').size())
---------------------------------------------------------------------
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',
   periods=10), columns=list('ABCD'))

df.plot()
-----------------------------------------------------------------

import pandas as pd
print(pd.Timedelta("2 days 2 hours 15 minutes 30 seconds"))
----------------------------------------------------------------

import pandas as pd
print(pd.Timedelta(6, unit='h'))
------------------------------------------------------------

import pandas as pd
print(pd.Timedelta(days=2))
--------------------------------------------------------------

import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))

print (df)
---------------------------------------------------------------

import pandas as pd

s=pd.Series(pd.date_range('2012-1-1',periods=3,freq='D'))
td=pd.Series([pd.Timedelta(days=i) for i in range(3)])
df=pd.DataFrame(dict(A=s,B=td))
print(df)
-------------------------------------------------------------

import pandas as pd
print(pd.date_range('1-1-2011',periods=5))
---------------------------------------------------------------

import pandas as pd
print(pd.date_range('1-1-2011',periods=5))
--------------------------------------------------------------

import pandas as pd

one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5'],
   'Marks_scored':[98,90,87,69,78]},
   index=[1,2,3,4,5])

two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5'],
   'Marks_scored':[89,80,79,97,88]},
   index=[1,2,3,4,5])
print( pd.concat([one,two]))
----------------------------------------------------------------

import pandas as pd

one=pd.DataFrame({
    'Name':['Alex','Amy','Allen','Alice','Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
    'marks_scored':[98,90,87,69,78]},
    index=[1,2,3,4,5])

two=pd.DataFrame({
    'Name':['Billy','Brain','Bran','Bryce','Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
    'marks_scored':[89,80,79,97,88]},
    index=[1,2,3,4,5])
print(pd.concat([one,two],keys=['x','y']))
---------------------------------------------------------------

import pandas as pd
print(pd.datetime.now())
------------------------------------------------------------

import pandas as pd
print(pd.Timestamp(21-1-2019))
--------------------------------------------------------------

def   outer() :
    print("Outer function running,...")
    def  inner() :
        print("Executing inner function")
    print("and outer funtion returning inner function")
    return inner

f1=outer()
f1()
f1()
inner()
---------------------------------------------------------

def outer():
    print("outer function running,.....")
    def inner():
        print("executing inner function")
    print("and outer function returning inner function")
    return inner
f1=outer()
f1()
f1()
inner()
-----------------------------------------------------------

def outer():
    print("outer function running,....")
    def inner():
        print("executing inner function")
    print("and outer function returning inner function")
    return inner
f1=outer()
f1()
f1()
inner()
-----------------------------------------------------------

def outer():
    print("outer function running,.......")
    def inner():
        print("executing inner function")
    print("and outer function returning inner function")
    return inner
f1=outer()
f1()
f1()
inner
----------------------------------------------------------

def   outer() :
    print("Outer function started,....")
    def   inner() :
        print("Called inner function")
    print("Outer function returning inner function,....")
    return inner

f1=outer()
print(type(f1),f1)
f1()
---------------------------------------------------------

def outer():
    print("outer function started,...")
    def inner():
        print("called inner function")

    print("outer function returning inner function")
    return inner
f1=outer()
print(type(f1),f1)
f1()
--------------------------------------------------------


def   f1() :
    print("Outer function starts,....")
    def   add(a,b) :
        print("Sum =",a+b)
        print("Average = ",(a+b)/2)

    print("Calling inner function,....")
    add(100,200)
    add(10,20)
    add(125,225)

f1()

add(10,20)
------------------------------------------------------

def f1():
    print("outer function stars,....")
    def add(a,b):
        print("sum=",a+b)
        print("average=",(a+b)/2)

    print("calling inner function,..")
    add(100,200)
    add(10,20)
    add(125,125)
f1()
add(10,20)
-------------------------------------------------------

def   wishdecor(func) :
    def  inner(name) :
        if  name=="Heroine" :
            func(name)
            print("Hi!What is your next movie?")
        else :
            func(name)
    return inner


@wishdecor
def   wish(name) :
    print("Hi, How are you doing?",end=" ")

wish("housewife")
print()
wish("Workingwomen")
print()
wish("Heroine")
----------------------------------------------------------

def wishdecor(func):
    def inner(name):
        if name=="Heroine":
            func(name)
            print("Hi!what is your next movie?")
        else:
            func(name)
    return inner
@wishdecor
def wish(name):
    print("Hi,How are you doing?",end=" ")

wish("housewife")
print()
wish("Workingwomen")
print()
wish("Heroine")
--------------------------------------------------------------

def wishdecor(func):
    def inner(name):
        if name=="Heroine":
            func(name)
            print("Hi!what is your next moviw?")
        else:
            func(name)
    return inner
@wishdecor
def wish(name):
    print("Hi,How are you doing?",end=" ")

wish("housewife")
print()
wish("Workingwomen")
print()
wish("Heroine")
----------------------------------------------------------------

def wishdecor(func):
    def inner(name):
        if name=="Heroine":
            func(name)
            print("Hi!what is your next movie")
        else:
            func(name)
    return inner
@wishdecor
def wish(name):
    print("Hi!,How are you doing?",end="")

wish("housewife")
print()
wish("Workingwomen")
print()
wish("Heroine")
------------------------------------------------------------------

def wishdecor(func):
    def inner(name):
        if name=="Heroine":
            func(name)
            print("Hi!what is your next movie")
        else:
            func(name)
    return inner
@wishdecor
def wish(name):
    print("Hi!,How are you doing?",end=" ")
wish("housewife")
print()
wish("workingwomen")
print()
wish("Heroine")
------------------------------------------------------------------

def wishdecor(func):
    def inner(name):
        if name=="Heroine":
            func(name)
            print("Hi!what is your next movie")
        else:
            func(name)
    return inner
@wishdecor
def wish(name):
    print("Hi!,How are you doing?",end=" ")
wish("housewife")
print()
wish("workingwomen")
print()
wish("Heroine")
---------------------------------------------------------

def wishdecor(func):
    def inner(name):
        if name=="Heroine":
            func(name)
            print("Hi!what is your next movie")
        else:
            func(name)
    return inner
@wishdecor
def wish(name):
    print("Hi!,how are you doing?",end=" ")
wish("housewife")
print()
wish("workingwomen")
print()
wish("Heroine")
----------------------------------------------------------

def wishdecor(func):
    def inner(name):
        if name=="Heroine":
            func(name)
            print("Hi!what is your next movie")
        else:
            func(name)
    return inner
@wishdecor
def wish(name):
    print("Hi!,how are you doing?",end=" ")
wish("housewife")
print()
wish("workingwomen")
print()
wish("Heroine")
------------------------------------------------------------

def wishdecor(func):
    def inner(name):
        if name=="Heroine":
            func(name)
            print("Hi!what is your next movie")
        else:
            func(name)
    return inner
@wishdecor
def wish(name):
    print("HI!how are you doing?",end=" ")
wish("housewife")
print()
wish("workingwomen")
print()
wish("Heroine")
-----------------------------------------------------------------

def wishdecor(func):
    def inner(name):
        if name=="Heroine":
            func(name)
            print("Hi!what is your next movie")
        else:
            func(name)
    return inner
@wishdecor
def wish(name):
    print("Hi!how are you doing?",end=" ")
wish("housewife")
print()
wish("workingwomen")
print()
wish("Heroine")
---------------------------------------------------------------

def wishdecor(func):
    def inner(name):
        if name=="Heroine":
            func(name)
            print("Hi!what is your next movie")
        else:
            func(name)
    return inner
@wishdecor
def wish(name):
    print("Hi!what are you doing?",end=" ")
wish("housewife")
print()
wish("workingwomen")
print()
wish("Heroine")
-------------------------------------------------------------

def   wishdecor(a) :
    def  inner(name) :
           
            print("Hi!What is your next movie?")
    
    return inner 


def   wish(name) :
    print("Hi, How are you doing?")

x=wishdecor(wish)
wish("housewife")
wish("Workingwomen")
wish("Heroine")

x("Heroine")
x("bussinesswomen")
---------------------------------------------------------------

def wishdecor(a):
    def inner(name):
        print("Hi!what is your next movie?")
    return inner
def wish(name):
    print("Hi,how are you doing?")

x=wishdecor(wish)
wish("housewife")
wish("workingwomwn")
wish("Heroine")

x("Heroine")
x("businesswomen")
----------------------------------------------------------------------

def wishdecor(a):
    def inner(name):
        print("Hi!what is your next movie?")
    return inner
def wish(name):
    print("Hi!,how are you doing?")

x=wishdecor(wish)
wish("housewife")
wish("workingwomen")
wish("Heroine")

x("Heroine")
x("businesswomen")
---------------------------------------------------------------------

def wishdecor(a):
    def inner(name):
        print("Hi!what is your next movie")
    return inner
def wish(name):
    print("Hi!how are you doing")

x=wishdecor(wish)
wish("housewife")
wish("workingwomen")
wish("Heroine")

x("Heroine")
x("businesswomen")
--------------------------------------------------------------

def   smart_divide(func) :
    def   inner(a,b) :
        if  b==0 :
            print("Sorry,Division by zero not possible.")
        else :
            func(a,b)
    return inner

@smart_divide
def   divide(a,b) :
    print("Division : ",a/b)

divide(100,10)

divide(50,0)

divide(10,3)
-------------------------------------------------------

def smart_divide(func):
    def inner(a,b):
        if b==0:
            print("sorry,Division by zero not possible")
        else:
            func(a,b)
    return inner
@smart_divide
def divide(a,b):
    print("Division :",a/b)

divide(100,10)
divide(50,0)
divide(10,3)
------------------------------------------

def smart_divide(func):
    def inner(a,b):
        if b==0:
            print("sorry,Division by zero not possible")
        else:
            func(a,b)
    return inner
@smart_divide
def divide(a,b):
    print("Division: ",a/b)
divide(100,10)
divide(50,0)
divide(10,3)
--------------------------------------------


import time
def  facial(func) :
    def  inner() :
        print("I am in facial section")
        time.sleep(2)
        func()
    return  inner

def  hairstyle(func) :
    def  inner() :
        print("Now I am into hair style section")
        time.sleep(2)
        func()
    return inner

def  makeup(func) :
    def  inner() :
        print("now I am taking makeup")
        time.sleep(2)
        func()
    return inner
@facial
@hairstyle
@makeup
def  getreadyforparty() :
    print("Lets go to the party")

getreadyforparty()
----------------------------------------------------

def   doublenumber(func) :
    def  inner() :
        x=func()
        return x*2
    return inner

def  triplenumber(func) :
    def  inner() :
        x=func()
        return x**3
    return inner

@triplenumber
@doublenumber
def    singlenumber() :
    return 10

print(singlenumber())
--------------------------------------------

class   Sample :
    __a=100
    b=200

    def   __f1(self) :
        print("I am private f1 function")
        
    def   f2(self) :
        print(" I am public f2,calling private f1")
        self.__f1()
        print("a=",Sample.__a)

x=Sample()
#print(x.__a)
#x.__f1()
x.f2()
print("b=",Sample.b)
------------------------------------


class  A :
    
    def __init__(self) :
       print("Hey, I am a constructor")
        
    def  f1(self) :
       print("I am f1")
     

a=A()
b=A()
c=A()
a.f1()
-----------------------------------\

class A:
    a=100
    def f1(self) :
        print(" I am f1")
class B :
    b=200
    def f2(self) :
        print( "I am f2")
class C(A,B) :
    c=300
    def f3(self) :
        print( "I am f3")
        print( "a=",C.a,"b=",C.b,"c=",C.c)
        #print( "a=",A.a,"b=",B.b,"c=",C.c)
x=C()
x.f1()
x.f2()
x.f3()
----------------------------------


class A:
    
    def f1(self) :
        print(" I am Parent class f1")
class B :
    
    def f2(self) :
        print( "I am f2")
class C(A,B) :
    
    def f1(self) :
        print( "I am Child class f1")
        
x=C()
x.f1() # I am Child class f1
x.f2()
--------------------------------

class   A:
    __a=100
    def  __f1(self):
        print(" I am private f1 method")
    def  f2(self):
        print("I am public f2 method")
        print("I am calling private f1 method :")
        self.__f1()
        print(" I am reading private __a value : ",A.__a)
class B(A) :
    def f3(self) :
        print("I am child class public f3 method")
        
x=B()
x.f3()
x.f2()
--------------------------------------
class A:
    def __init__(self) :
        print(" I am Parent class constructor")
class B(A) :
    def  f1(self) :
        print("I am f1")
    def __init__(self) :
        A.__init__(self)        
        print("I am Child class constructor")
       
    
b1=B()
b2=B()
--------------------------------------

# Example of Destructor

class   Sample :
    def  __init__(self) :
        print("I am a constructor")
    def  __del__(self) :
        print("I am a destructor")


def  f1() :
    a=Sample()
    b=Sample()


x=Sample()
f1()
y=Sample()
del  x
del  y
------------------------------------

class   Employee :
    cnt=0
    def  __init__(self) :
        Employee.cnt+=1
        print("Employee joined :",Employee.cnt)
    def  __del__(self) :
        Employee.cnt-=1
        print("Removed employee :",Employee.cnt)


def  f1() :
    a=Employee()
    b=Employee()


x=Employee()
f1()
y=Employee()
del x
del y
-----------------------------------------
'''
class  Company :
    cname="Tecnosoft"   # class variables / static variables
    phno="9966422225"
    addr="Ameerpet,Hyderabad"

    def   __init__(self,empno,ename,job,sal) :  #  constructor method
        self.empno=empno  # instance variables/ non static variables
        self.ename=ename
        self.job=job
        self.sal=sal
    def  DisplayEmpDetails(self): # instance method
        print(self.__dict__)
    @classmethod
    def  CompanyDetails(cls) :  # class method
        print(" Company Name : {},Phno:{},Addr:{}".format(Company.cname,Company.phno,Company.addr))
    @staticmethod
    def   bonus() :
        print("This year no bonus.")
    
x=Company(1,'Ganesh','President',90000)
y=Company(2,'Hari','Analyst',85000)
x.DisplayEmpDetails()
y.DisplayEmpDetails()
Company.CompanyDetails()
Company.bonus()




































































































    

























































































































































































































































































































































































































































