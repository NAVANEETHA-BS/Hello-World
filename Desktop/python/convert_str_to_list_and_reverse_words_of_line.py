#converting string to list and list to string and reverse words

x=input("enter a string : ")
x=x.split()
#print(x)
x=x[::-1]
y=" ".join(x)
print(y)
