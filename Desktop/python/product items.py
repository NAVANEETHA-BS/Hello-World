# accept no. of products
'''
no. of products==3  => 50% discount
no. of products==2  => 40% discount
no. of products==1  => 30% discount
'''

n=int(input("How many shirts do you want to buy[max : 3] ? :"))
if n==3:
    (sh1,sh1_pr)=input("Enter shirt brand name,price : ").split()
    (sh2,sh2_pr)=input("Enter shirt brand name,price : ").split()
    (sh3,sh3_pr)=input("Enter shirt brand name,price : ").split()
    total=float(sh1_pr)+float(sh2_pr)+float(sh3_pr)
    if sh1==sh2 and sh2==sh3:
        disc=total*50/100
        total=total-disc
    print("your bill is :",total)
elif n==2:
    
    (sh1,sh1_pr)=input("Enter shirt brand name,price : ").split()
    (sh2,sh2_pr)=input("Enter shirt brand name,price : ").split()
    total=float(sh1_pr)+float(sh2_pr)
    if sh1==sh2:
        disc=total*40/100
        total=total-disc
    print("your bill is :",total)
elif n==1:
    
    (sh1,sh1_pr)=input("Enter shirt brand name,price : ").split()
    total=float(sh1_pr)
    disc=total*30/100
    total=total-disc
    print("your bill is :",total)
    
