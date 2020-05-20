# single dimensional array
'''
import numpy as np
a=np.array([1,2,3])
print(a)

o/p:[1,2,3]

# multi-dimensional array
import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(a)

o/p:
    [[1 2 3]
 [4 5 6]]
'''
#memory example(list)
'''
import numpy as np
import time
import sys
s=range(1000)
print(sys.getsizeof(5)*len(s))

o/p: 14000
'''

#memory example(numpy)
'''
import numpy as np
import time
import sys
d=np.arange(1000)
print(d.size*d.itemsize)

o/p: 4000
'''
#speed(list)
'''
import time
import sys

size=1000000

l1=range(size)
l2=range(size)

start=time.time()
result=[(x,y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)

o/p:289.81876373291016
'''
#speed(numpy)
'''
import numpy as np
import time
import sys

size=1000000

a1=np.arange(size)
a2=np.arange(size)

start=time.time()
result=a1+a2
print((time.time()-start)*1000)

o/p: 32.03439712524414
'''
#ndim
'''
import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)

o/p:2
'''
#itemsize
'''
import numpy as np
a=np.array([1,2,3])
print(a.itemsize)

0/p:4
'''
#dtype
'''
import numpy as np
a=np.array([1,2,3])
print(a.dtype)

o/p:int32
'''

#size and shape
'''
import numpy as np
a=np.array([(1,2,3,4,5,6)])
print(a.size)
print(a.shape)

o/p:
    6
    (1,6)
'''

#reshape
'''
import numpy as np
a=np.array([(8,9,10),(11,12,13)])
print(a)
a=a.reshape(3,2)
print(a)

o/p:[[ 8  9 10]
 [11 12 13]]
[[ 8  9]
 [10 11]
 [12 13]]

'''

#slicing
'''
import numpy as np
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a[0,2])

o/p:3
'''
'''
import numpy as np
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a[0:,2])

o/p:[3,5]
'''
'''
import numpy as np
a=np.array([(8,9),(10,11),(12,13)])
print(a[0:2,1])

o/p:[9,11]
'''
#linspace
'''
import numpy as np
a=np.linspace(1,3,10)
print(a)

o/p:[1.         1.22222222 1.44444444 1.66666667 1.88888889 2.11111111
 2.33333333 2.55555556 2.77777778 3.        ]
'''
#max/min/sum
'''
import numpy as np
a=np.array([1,2,3])
print(a.min())
print(a.max())
print(a.sum())

o/p:1
3
6
'''
'''
import numpy as np
a=np.array([(1,2,3),(3,4,5)])
print(a.sum(axis=0))

o/p:[4 6 8]
'''
#square root ans standard deviation
'''
import numpy as np
a=np.array([(1,2,3),(3,4,5)])
print(np.sqrt(a))
print(np.std(a))

o/p:[[1.         1.41421356 1.73205081]
 [1.73205081 2.         2.23606798]]
1.2909944487358056
'''
#addition
'''
import numpy as np
x=np.array([(1,2,3),(3,4,5)])
y=np.array([(1,2,3),(3,4,5)])
print(x+y)

o/p:[[ 2  4  6]
 [ 6  8 10]]
'''
'''
import numpy as np
a=np.array([(1,2,3),(3,4,5)])
b=np.array([(1,2,3),(3,4,5)])
print(a-b)
print(a*b)
print(a/b)

o/p:[[0 0 0]
 [0 0 0]]
[[ 1  4  9]
 [ 9 16 25]]
[[1. 1. 1.]
 [1. 1. 1.]]
'''

#vertical and horizontal stacking
'''
import numpy as np
x=np.array([(1,2,3),(3,4,5)])
y=np.array([(1,2,3),(3,4,5)])
print(np.vstack((x,y)))
print(np.hstack((x,y)))

o/p:
    [[1 2 3]
 [3 4 5]
 [1 2 3]
 [3 4 5]]
[[1 2 3 1 2 3]
 [3 4 5 3 4 5]]
'''
#ravel(converts into single column)
'''
import numpy as np
x=np.array([(1,2,3),(3,4,5)])
print(x.ravel())

o/p:[1 2 3 3 4 5]
'''
#numpy special functions(sine,cosine,tan,log etc)
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
y=np.tan(x)
plt.plot(x,y)
plt.show()
'''
#exponential
'''
import numpy as np
a=np.array([(1,2,3)])
print(np.exp(a))

o/p:[[ 2.71828183  7.3890561  20.08553692]]
'''

#logarithmic
'''
import numpy as np
a=np.array([(1,2,3)])
print(np.log10(a))

o/p:[[0.         0.30103    0.47712125]]
'''
#write a numpy program to get the n largest values of an array
'''
import numpy as np
x=np.arange(10)
print("original array",x)
np.random.shuffle(x)
n=1
print(x[np.argsort(x)[-n:]])

o/p:
original array [0 1 2 3 4 5 6 7 8 9]
[9]
'''

#Write a NumPy program to find the closest value (to a given scalar) in an array
'''
import numpy as np
x=np.arange(100)
print("original array",x)
a=np.random.uniform(0,100)
print("value to compare :")
print(a)
index=(np.abs(x-a)).argmin()
print(x[index])

o/p:
    original array [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
 96 97 98 99]
value to compare :
95.37502397348129
95
'''

# Write a NumPy program to convert cartesian coordinates to polar coordinates of a random 10x3 matrix representing cartesian coordinates.
'''
import numpy as np
z= np.random.random((10,3))
x,y = z[:,0], z[:,1]
print(x)
print(y)
r = np.sqrt(x**2+y**2)
t = np.arctan2(y,x)
print(r)
print(t)

o/p:
[0.81075124 0.02991446 0.30974246 0.76174873 0.60267537 0.20933587
 0.0215134  0.90318718 0.97563671 0.62071675]
[0.39521759 0.75288802 0.96821579 0.61948579 0.04092822 0.42083104
 0.4527394  0.368403   0.60267387 0.90266924]
[0.9019504  0.75348208 1.01655409 0.98184712 0.60406351 0.47002156
 0.45325025 0.97543213 1.14677058 1.09549124]
[0.45357414 1.53108427 1.26117451 0.68276312 0.06780678 1.10920324
 1.52331375 0.38729142 0.55334976 0.96840995]
'''

#write a python program to find most frequent value in the array
'''
import numpy as np
x=np.random.randint(0,10,40)
print("original array : ",x)
print("most frequent value in the array : ")
print(np.bincount(x).argmax())

o/p:
original array :  [8 7 4 6 3 4 2 7 4 1 1 9 4 3 9 0 9 1 8 8 8 1 2 6 2 3 7 4 5 1 0 6 2 3 5 4 9
 0 7 5]
most frequent value in the array : 
4
'''
#Write a NumPy program to find point by point distances of a random vector with shape (10,2) representing coordinates.
'''
import numpy as np
a=np.random.random((10,2))
x,y=np.atleast_2d(a[:,0],a[:,1])
print(x)
print(y)
d=np.sqrt((x-x.T)**2 + (y-y.T)**2)
print(d)

o/p:
[[0.         0.40042551 0.97051396 0.51623725 0.63113154 0.51530776
  0.41123565 0.81981293 0.28700272 0.97203531]
 [0.40042551 0.         0.94237615 0.22036923 0.6809259  0.5022781
  0.07585226 0.48834696 0.1422807  0.636204  ]
 [0.97051396 0.94237615 0.         1.15949816 0.34662026 0.46819424
  1.01793237 0.75197582 1.00513539 0.79218808]
 [0.51623725 0.22036923 1.15949816 0.         0.90055654 0.72251306
  0.14903778 0.61927882 0.23747255 0.74954027]
 [0.63113154 0.6809259  0.34662026 0.90055654 0.         0.18125017
  0.75197198 0.67921617 0.71008641 0.78091245]
 [0.51530776 0.5022781  0.46819424 0.72251306 0.18125017 0.
  0.574679   0.53801295 0.54307482 0.65927504]
 [0.41123565 0.07585226 1.01793237 0.14903778 0.75197198 0.574679
  0.         0.54276645 0.12646038 0.68643793]
 [0.81981293 0.48834696 0.75197582 0.61927882 0.67921617 0.53801295
  0.54276645 0.         0.6267567  0.15255701]
 [0.28700272 0.1422807  1.00513539 0.23747255 0.71008641 0.54307482
  0.12646038 0.6267567  0.         0.77620902]
 [0.97203531 0.636204   0.79218808 0.74954027 0.78091245 0.65927504
  0.68643793 0.15255701 0.77620902 0.        ]]

'''

#Write a NumPy program to create random vector of size 15 and replace the maximum value by -1.
'''
import numpy as np
x=np.random.random(15)
print("original array : ",x)
x[x.argmax()]=-1
print("maximum value replaced by -1 : ",x)

o/p:
original array :  [0.89385892 0.01422781 0.86205776 0.89417307 0.31533247 0.79123489
 0.20491108 0.96376329 0.72375699 0.45934232 0.84381242 0.03604342
 0.89841598 0.56437696 0.17564942]
maximum value replaced by -1 :  [ 0.89385892  0.01422781  0.86205776  0.89417307  0.31533247  0.79123489
  0.20491108 -1.          0.72375699  0.45934232  0.84381242  0.03604342
  0.89841598  0.56437696  0.17564942]

'''
#Write a NumPy program to check two random arrays are equal or not.
'''
import numpy as np
x=np.random.randint(0,2,6)
print("first array : ",x)
y=np.random.randint(0,2,6)
print("second array : ",y)
print("Test above two conditions equal or not")
array_equal=np.allclose(x,y)
print(array_equal)

o/p:
first array :  [0 1 0 1 0 0]
second array :  [1 1 1 0 1 1]
Test above two conditions equal or not
False
'''















































































































































































































































































































































































































































