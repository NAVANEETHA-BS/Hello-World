
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
y=[]
for i in x:
    #print(i[4])
    y.append(i[4])
y=set(y)
y=list(y)
print(y)
sum=0
#k=0
for p in y:
    for j in x:
    #print(j[4])
    #if j[4] in y:
        if p==j[4]:
            sum=sum+j[3]
            break
        print(sum)
'''        
l=[]
for i in x:
    #print(i[4])
    l.append(i[4])
l=set(l)
#print(l)
l=list(l)
print(l)


















    








