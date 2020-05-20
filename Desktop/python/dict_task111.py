
'''
x=[[101,'ganesh','manager',90000,10],
   [102,'hari','Analyst',80000,20],
   [103,'padma','programmer',70000,30],
   [104,'sai','manager',90000,20],
   [105,'A','programmer',60000,10],
   [106,'B','Analyst',50000,30],
   [107,'C','programmer',70000,20],
   [108,'D','programmer',30000,10],
   [109,'E','manager',40000,10]]

dept=[]
d={}
l=[]
l1=[]
for i in x:
    j=(i[2])
    l.append(j)
#print(l)
l=set(l)
#print(l)
for k in l:
    #print(k) 
    l1.append(k)
print(l1)

sum=0
for p in l1:
    for q in x:
        if p==q[2]:
            sum=sum+q[3]
    print(sum)
    d[p]=sum
    #print(d)
    sum=0
print(d)

'''

x=[[101,'ganesh','manager',90000,10],
   [102,'hari','Analyst',80000,20],
   [103,'padma','programmer',70000,30],
   [104,'sai','manager',90000,20],
   [105,'A','programmer',60000,10],
   [106,'B','Analyst',50000,30],
   [107,'C','programmer',70000,20],
   [108,'D','programmer',30000,10],
   [109,'E','manager',40000,10]]


dept=[]
d={}
l=[]
l1=[]
for i in x:
    j=(i[2])
    r=i[4]
    l.append(j)
    dept.append(r)
#print(l)
l=set(l)
#print(l)
for k in l:
    #print(k) 
    l1.append(k)
print(l1)

sum=0
for p in l1:
    for q in x:
        if p==q[2]:
            sum=sum+q[3]
    print(sum)
    d[p]=sum
    #print(d)
    sum=0
print(d)
print(dept)
dept=list(set(dept))
print(dept)

            
            


















    



























