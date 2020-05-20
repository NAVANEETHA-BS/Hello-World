'''
name1 = 'ram'
name2 = 'janu'

name1list = list(name1.upper())
name2list = list(name2.upper())

for l in name1list:
    if l in name2list:
        idx = name1list.index(l)
        name1list[idx] = '_'
        idx = name2list.index(l)
        name2list[idx] = '_'
print(name1list)
print(name2list)

names = name1list +name2list
count = 0

for l in names:
    if(l!='_' and l!=' '):
        count+=1
print(count)
f = list('FLAMES')
index = 0
while len(f) > 1:
    for i in range(count):
        index += 1
        if index > len(f):
            index = 1
    f.remove(f[index-1])
    index-=1
print(f)
---------------------------------------------------------------------------

name1 = "ram"
name2 = "janu"
name1list = list(name1.upper())
name2list = list(name2.upper())
for l in name1list:
    if l in name2list:
        idx = name1list.index(l)
        name1list[idx] = '_'
        idx = name2list.index(l)
        name2list[idx] = '_'
print(name1list)
print(name2list)

names = name1list + name2list
cnt = 0
for l in names:
    if(l!=' ' and l!='_'):
        cnt+=1
print(cnt)

f = list('FLAMES')
index = 0
for i in range(cnt):
    index += 1
    if index > len(f):
        index = 1
    f.remove(f[index-1])
    index-=1
print(f)
---------------------------------------------------------------


name1 = 'ram'
name2 = 'janu'
name1list = list(name1.upper())
name2list = list(name2.upper())
for l in name1list:
    if l in name2list:
        idx = name1list.index(l)
        name1list[idx] = '_'
        idx = name2list.index(l)
        name2list[idx] = '_'
print(name1list)
print(name2list)

names = name1list + name2list
cnt = 0
for l in names:
    if(l!=" " and l!="_"):
        cnt+=1
print(cnt)

f=list('FLAMES')
index = 0
for i in range(cnt):
    index+=1
    if index >len(f):
        index = 1
    f.remove(f[index-1])
    index-=1
print(f)
------------------------------------------------------------------
'''
name1 = 'ram'
name2 = 'janu'
name1list = list(name1.upper())
name2list = list(name2.upper())
for l in name1list:
    if l in name2list:
        idx = name1list.index(l)
        name1list[idx]='_'
        idx = name2list.index(l)
        name2list[idx]='_'
print(name1list)
print(name2list)

names = name1list + name2list
cnt = 0
for l in names:
    if(l!=' ' and l!='_'):
        cnt += 1
print(cnt)

f = list('FLAMES')
index=0
for i in range(cnt):
    index+=1
    if index>len(f):
        index = 1
    f.remove(f[index-1])
    index-=1
print(f)
    
    




































    


























































































    
