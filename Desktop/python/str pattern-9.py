'''
****upper limit should not be negative number in python-3******
9)tecno

oncet
once
onc
on
o
'''
x=input("enter a string : ")
l=len(x)
print(x[::-1])

for i in range(0,l):
    print(x[(l-1):i:-1])
    
