x=[[101,'ganesh','manager',90000,10],
   [102,'hari','analyst',80000,20],
   [103,'padma','programmer',70000,30],
   [104,'sai','manager',90000,20],
   [105,'A','programmer',60000,10],
   [106,'B','Analyst',50000,30],
   [107,'C','programmer',70000,20],
   [108,'D','programmer',30000,10],
   [109,'E','manager',40000,10]]
'''
l=[]
for i in x:
    #print(i[4])
    l.append(i[4])
l=list(set(l))
print(l)
index=0
cnt=0
for j in x:
    print(j[4])
    while index<len(l):
        if l[index]==j[4]:
            cnt=cnt+j[3]
        index+=1
        print(cnt)
-------------------------------------------------

l=[]
for i in x:
    #print(i[4])
    l.append(i[4])
l=list(set(l))
print(l)
index=0
cnt=0
while index<len(l):
    for j in x:
    #print(j[4])
        if l[index]==j[4]:
            cnt=cnt+j[3]
    
    print(cnt)
    cnt=0
    index+=1

---------------------------------------------------

d={}
l=[]
for i in x:
    #print(i[4])
    l.append(i[4])
l=list(set(l))
print(l)
index=0
cnt=0
while index<len(l):
    for j in x:
    #print(j[4])
        if l[index]==j[4]:
            cnt=cnt+j[3]
            d[j[4]]=cnt
            
            
    print(cnt)
    print(d) 
    cnt=0
    index+=1

--------------------------------------
x=[[101,'ganesh','manager',90000,10],
   [102,'hari','Analyst',80000,20],
   [103,'padma','programmer',70000,30],
   [104,'sai','manager',90000,20],
   [105,'A','programmer',60000,10],
   [106,'B','Analyst',50000,30],
   [107,'C','programmer',70000,20],
   [108,'D','programmer',30000,10],
   [109,'E','manager',40000,10]]

d={}
dept=[]
job=[]
for i in x:
    #print(i[4])
    dept.append(i[4])
    dept=list(set(dept))
print(dept)
for j in x:
    job.append(j[2])
    job=list(set(job))
print(job)

index=0
while index<len(dept):
    d[dept[index]]=job
    index+=1
print(d)

o/p:
[10, 20, 30]
['Analyst', 'manager', 'programmer']
{10: ['Analyst', 'manager', 'programmer'],
 20: ['Analyst', 'manager', 'programmer'],
 30: ['Analyst', 'manager', 'programmer']}
--------------------------------------------
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

d={}
dept=[]
job=[]
for i in x:
    #print(i[4])
    dept.append(i[4])
    dept=list(set(dept))
print(dept)
for j in x:
    job.append(j[2])
    job=list(set(job))
print(job)

index=0
while index<len(dept):
    d[dept[index]]=job
    index+=1
print(d)

d1={}
while index<len(job):
    for j in x:
    #print(j[4])
        if job[index]==j[4]:
            cnt=cnt+job[3]
            d1[job[4]]=cnt
        print(d1)
for m in d1:
    print(m)
       
    
    


























    
    

    
    















