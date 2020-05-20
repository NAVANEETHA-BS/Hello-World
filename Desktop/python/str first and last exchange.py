'''
python program to form a new string where the first character and last
character have been exchanged

ex:python
expected output:nythop
'''
x=input("enter a string : ")
if x!="":
    n=len(x)
    x=x[-1]+x[1:-1]+x[0]
    print(x)
else:
    print("plz enter a string : ")
