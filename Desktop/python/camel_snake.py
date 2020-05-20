'''
x = "MyNameIsNeetha"
y = []
for i in x:
    if i.isupper():
        print(i)
        y.append(i)
#print(y)
    for j in y:
        if i == j:
            x = x.split(j)
            print(x)
'''

import re
x = "MyNameIsNeetha"
for i in x:
    if i in "MYIN":
        x.split(i)
        print(x)
y = x.lower()
print(y)
