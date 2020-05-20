'''
python program to take  in a string and replace every blank space with hyphen
eg: welcome to python class
expected o/p:welcome-to-python-class
'''

x=input("enter a string : ")
if x!="":
    x=x.replace(" ","-")
    print(x)
else:
    print("plz enter a string : ")
