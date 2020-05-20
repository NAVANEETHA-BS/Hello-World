# leap year or not
year=int(input("enter a 4 digit year"))
if year%4==0 and year%100!=0 or year%400==0:
    print(year,"year is a leap year")
else:
    print(year,"not a leap year")
