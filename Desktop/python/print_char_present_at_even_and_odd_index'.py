'''
s="navaneetha"
i=0
while i<len(s):
    print("char present at even index :",s[i])
    i=i+2

i=1
while i<len(s):
    print("char present at odd index :",s[i])
    i=i+2
---------------------------------------------------
'''
#o/p:char present at even index : nvneh
#    char present at odd index : aaeta

s="navaneetha"
print("char present at even index :",s[::2])
print("char present at odd index :",s[1::2])
