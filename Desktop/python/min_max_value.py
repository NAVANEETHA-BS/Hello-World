x=[10,2,3,23,56,787,1]
a=x[0]
b=x[0]

for i in x:
    if i < a:
        a=i

    if i > b:
        b=i
print("minimum value is : " ,a)
print("maximum value is : ",b)
