#accept a month and display number of days

month=input("enter a month :")

if month.upper()=="FEBRUARY" :
    print(month.upper(), "has 28/29 days.")
elif month.upper() in ("JANUARY","MARCH","MAY","JULY","AUGUST","OCTOBER","NOVEMBER"):
    print(month.upper(),"has 31 days.")
elif month.upper() in ("APRIL","JUNE","SEPTEMBER","NOVEMBER"):
     print(month.upper(),"has 30 days")
else:
     print("pls enter valid month name")
          
        



