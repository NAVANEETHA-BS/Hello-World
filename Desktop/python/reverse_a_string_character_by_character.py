'''
x=input("enter a string : ")
x=x[::-1]
print(x)
------------------------------------

x=input("enter a string : ")
r=reversed(x)
z="".join(r)
print(z)
------------------------------------
'''
s='neetha'
output=' '
i=len(s)-1
while i>0:
    output=output+s[i]
    i=i-1
print(output)
