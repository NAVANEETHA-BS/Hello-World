'''
import numpy as np
x=[1,2,3,4,5]
y=np.array(x)
print(y)
------------------------------

import numpy as np
x=[[1,2,3],[4,5,6],[7,8,9]]
y=np.array(x)
print(y)
-----------------------------------

import numpy as np
y=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(y)
----------------------------------------

import numpy as np
y=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(y)
---------------------------------------

import numpy as np
y=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='float')
print(y)
-------------------------------------------

import numpy as np
y=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='str')
print(y)
----------------------------------------------

import numpy as np
y=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='int')
print(y)
-----------------------------------------------

import numpy as np
y=np.array([[1,0,3],[4,5,6],[7,8,9]],dtype='bool')
print(y)
------------------------------------------------

import numpy as np
y=np.array([[1,2,'a'],['d',4,5],[7,8,9]],dtype='str')
print(y)
------------------------------------------------

import numpy as np
y=np.array([[1,2,3],[4,5,6],[7,8,9]])
z=y.astype('int')
print(z)
w=z.astype('float')
print(w)
q=w.astype('bool')
print(q)
r=q.astype('object')
print(r)
d=r.astype('str')
print(d)
------------------------------------------------------

import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='float')
print(x)
y=x.tolist()
print(y)
--------------------------------------------------

import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='int')
y=x.shape
print(y)
------------------------------------------------------
'''
import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='str')
y=x.size

print(y)
















































































