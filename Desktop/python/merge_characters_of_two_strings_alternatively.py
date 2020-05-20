# i/p:s1='navaneetha'
#     s2='teja'
# o/p:ntaevjaaneetha


s1=input("enter a string1 : ")
s2=input("enter a string2 : ")
output=''
i=0
j=0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
print(output)
