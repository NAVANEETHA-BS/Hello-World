

s='My Name Is Navaneetha'
l=s.split()
l1=[]
for word in l:
    r=word[::-1]
    l1.append(r)
    output=" ".join(l1)
print(output)
