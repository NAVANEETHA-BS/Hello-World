'''
4)Tecno

T
Te
Tec
Tecn
Tecno


x=input("enter a string : ")
l=1
for i in x:
    print(x[:l])
    l=l+1
'''

x=input("enter a string : ")
l=len(x)
for i in range(1,l+1):
    print(x[:i])
    
