'''
x=['apple','bell','cut','pig']
y='ap'
for i in enumerate(x):
    print(i)
    for j in enumerate(y):
        print(j)
        if i[0]==j[0]:
            print(i)
    break
---------------------------------------
'''

x=['apple','bell','cut','pig']
y=['ap']
for i,j in enumerate(x):
    print(i,j)
    for m,n in enumerate(y):
        print(m,n)
        if n==j:
            print(n)
    break
                
