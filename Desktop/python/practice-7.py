'''
x=['python','django','aws','unix','linux']
y=[len(i) for i in x]
y.sort()
#print(x)
#print(y)

for i in y:
    for j in x[:]:
        if i==len(j):
            print(j,end=" ")
            x.remove(j)
'''
x=[(9,7),(2,3),(4,1),(5,6),(3,5)]
y={}
for i in x:
    y=i[-1]=i[0]
keys=sorted(y.keys())
print(keys)
a=[]
for i in keys:
    a.append(y[i],i)
print(x)
print(a)
