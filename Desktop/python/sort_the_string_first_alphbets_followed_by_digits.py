#python program to print alphabet followed by digits

x=input("enter a string : ")
alphabet=[]
digit=[]
for ch in x:
    if ch.isalpha():
        alphabet.append(ch)
    else:
        digit.append(ch)
z="".join(sorted(alphabet)+sorted(digit))
print(z)
