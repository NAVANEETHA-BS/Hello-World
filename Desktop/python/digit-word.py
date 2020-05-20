'''
num = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
x = input("enter a number : ")
for i in (x):
    print(i, end="")
for n,m in num.items():
    #print(n)
    #print(type(n))
    #for i in range(1,10000):
    
        #print(x)
    if i==n:
        #print(i)
        print(m)
    


num = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
x = input("enter a number : ")
for n,m in num.items():
    #print(n)    
    for i in (x):
    #print(i)
        if i==n:
            #print(i,end="")
            print({i:m})
            #print(type(m))
           
            
print("length of x : ",len(x))
#if len(x)==3:
for p in num.values():
    print(p)
'''   
num = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
x = input("enter a number : ")
for n,m in num.items():
    #print(n)    
    for i in (x):
    #print(i)
        if i==n:
            #print(i,end="")
            #if i==n:
            #print(i,end="")
            print({i:num[m]})
            #print(type(m))


















