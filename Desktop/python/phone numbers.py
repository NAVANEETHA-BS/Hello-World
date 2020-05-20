#generating mobile numbers
'''
import random
i=0
while i<=15:
    i=i+1
    x=random.randint(6000000000,9999999999)
    print(x)
    
'''

#faker

from faker import Faker
x=Faker()
for i in range(1,11):
    print("Name : ",x.name())
    print("Phone Number : ",x.phone_number())
    print("Address : ",x.address())
    print("Job : ",x.job())
