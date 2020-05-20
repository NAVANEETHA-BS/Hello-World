'''
d=int(input("enter date : "))
m=int(input("enter month : "))
y=int(input("enter year : "))

if m in ['jan','mar','may','july','aug','oct','dec']:
    d=30
    print(d)
elif m in ['apr','jun','sep','nov']:
    d=31
    print(d)
else:
    d=28 or 29
    print(d)
print("date : "+d+"/"+m+"/"+y+"is valid")


d={'jan':30,'feb':28,'mar':30,'apr':31,'may':30,'jun':31,'jul':30,'aug':30,\
   'sep':30,'oct':30,'nov':31,'dec':30}
m=[
'''

date=input("Enter the date: ")
dd,mm,yy=date.split('/')
dd=int(dd)
mm=int(mm)
yy=int(yy)
if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max1=31
elif(mm==4 or mm==6 or mm==9 or mm==11):
    max1=30
elif(yy%4==0 and yy%100!=0 or yy%400==0):
    max1=29
else:
    max1=28
if(mm<1 or mm>12):
    print("Date is invalid.")
elif(dd<1 or dd>max1):
    print("Date is invalid.")
elif(dd==max1 and mm!=12):
    dd=1
    mm=mm+1
    print("The incremented date is: ",dd,mm,yy)
elif(dd==31 and mm==12):
    dd=1
    mm=1
    yy=yy+1
    print("The incremented date is: ",dd,mm,yy)
else:
    dd=dd+1
    print("The incremented date is: ",dd,mm,yy)
    
    
      
