'''
python program to remove the nth index character from a non-empty string
eg:hyderabad,nth index eg:4
expected output:hydeabad

'''
x=input("enter a string : ")
if x!="" :
    n=int(input("enter nth index to remove : "))
    l=len(x)
    if n<l:
        x=x[:n]+x[n+1:]
        print(x)
    else:
        print("oop's! index is out of range")

else:
    print("plz enter string")


