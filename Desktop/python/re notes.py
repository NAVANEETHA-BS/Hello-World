'''
import re
x="python released in 1989 year"
y=re.search(r"\b\d{4}\b",x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")


import re
x="python released in 1989 year"
y=re.search(r"\b\d{4}\b",x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")


import re
x="python released in 1989 year"
y=re.search(r"\b\d{4}\b",x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")


import re
x="python released in 1989 year"
y=re.search(r"\b\d{4}\b",x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")


import re
x="python released in 1989 year"
y=re.search(r"\b\d{4}\b",x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")


import re
x="python released in 1989 year"
y=re.search(r"\b\d{4}\b",x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")



import re
x="python released in 1989 year"
y=re.search(r"\b\d{4}\b",x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")



import re
x="python released in 1989 year"
y=re.search(r"\b\d{4}\b",x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")


import re
x="python released in 1989 year"
y=re.search(r"\b\d{4}\b",x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")


import re
x="python released in 1989 year"
y=re.search(r"\b\d{4}\b",x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")


import re
x="python released in 1989 year"
y=re.search(r'\b\d{4}\b',x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")


import re
x="python released in 1989 year"
y=re.search(r'\b\d{4}\b',x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")



import re
x="python released in 1989 year"
y=re.search(r"\b\d{4}\b",x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")


import re
x="python released in 1989 year"
y=re.search(r'\b\d{4}\b',x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")


import re
x="python released in 1989 year"
y=re.search(r'\b\d{4}\b',x)
print(y,type(y))
if y:
    print(y.group())
else:
    print("pattern not found")


import re
str="python i like 34 python.12345 python 18-08-2006 python \
# and 2345. it released in 1986."
y=re.search(r'\d{4}',str)
if y:
    print(y.group())
else:
    print("pattern not found")


import re
str="python i like 34 python. 12345 python 18-08-2006 python \
# and 2345. it released in 1986."
y=re.search(r'\d{4}',str)
if y:
    print(y.group())
else:
    print("pattern not found")


import re
str="python i like 34 python. 12345 python 18-08-2006 python \
# and 2345. it released in 1986."
y=re.search(r'\d{4}',str)
if y:
    print(y.group())
else:
    print("pattern not found")


import re
str="python i like 34 python. 12345 python 18-08-2006 python \
# and 2345. it released in 1986."
y=re.search(r'\d{4}',str)
if y:
    print(y.group())
else:
    print("pattern not found")


import re
str="python i like 34 python. 12345 python 18-08-2006 python \
# and 2345. it released in 1986."
y=re.findall(r'\b\d{2,5}\b',str)
print(y)


import re
str="python i like 34 python. 12345 python 18-08-2006 python \
# and 2345. it released in 1986."
y=re.findall(r'\b\d{2,5}\b',str)
print(y)


import re
str="python i like 9966422225 python.12345 09966422225 \
python 18-08-2006 python and +919966355554 2345. it \
8108765555 released 1234567890 in 1986"
#y=re.findall(r'\b[6789]\d{9}\b',str)
#y=re.findall(r'\b0?[6789]\d{9}\b',str)
y=re.findall(r'[+]\b91[6789]\d{9}\b',str)
print(y)


import re
str="python i like 192.168.0.1 python. 12345 09966433335 \
python 18-08-2006 python and 200.0.0.1 2345. it 8108765555 \
released 100.98.0.10 in 1986"
y=re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',str)
print(y)
           

import re
str="python i like 192.168.0.1 python. 12345 09966433335 \
python 18-08-2006 python and 200.0.0.1 2345. it 8108765555 \
released 100.98.0.10 in 1986"
y=re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',str)
print(y)


import re
x=["hello python","it is simple","it is easy","it is portable","it is oss"]
for i in x:
    y=re.search('[aeiou]$',i)
    if y:
        print(i)



import re
x=["hello python","it is simple","it is easy","it is portable","it is oss"]
for i in x:
    y=re.search('[aeiou]$',i)
    if y:
        print(i)



#9440381092


import re
x="soft is bc@gmail.com leading training tecno123@yahoo.in institute \
sree.tecno-soft@python.org in ameerpet"
k=re.findall(r'\b[\w.-]+@[\w.-]+\.[a-z]{2,3}\b',x)
#k=re.findall(r'\b[\w.-]{4,32}@[\w.-]{4,32}\.[a-z]{2,3}\b',x)
print(k)


import re
x="soft is bc@gmail.com leading training tecno123@yahoo.in institute \
sree.tecno-soft@python.org in ameerprt"
k=re.findall(r'\b[\w.-]+@[\w.-]+\.[a-z]{2,3}\b',x)
#k=re.findall(r'\b[\w.-]{4,32}@[\w.-]{4,32}\.[a-z]{2,3}\b',x)
print(k)
'''

import re
x="soft is bc@gmail.com leading training tecno123@yahoo.in institute \
sree.tecno-soft@python.org in ameerpet"
#k=re.findall(r'\b[\w.-]+@[\w.-]+\.[a-z]{2,3}\b',x)
k=re.findall(r'\b[\w.-]{4,32}@[\w.-]{4,32}\.[a-z]{2,3}\b',x)
print(k)

































































































    










    





















