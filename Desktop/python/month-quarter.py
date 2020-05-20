# accept month name and display its quarter
month=input("enter a month name")

if month.upper() in ("JANUARY","FEBRUARY","MARCH"):
    print("first quarter")
elif month.upper() in ("APRIL","MAY","JUNE"):
    print("second quarter")
elif month.upper() in ("JULY","AUGUST","SEPTEMBER"):
    print("third quarter")
elif month.upper() in ("OCTOBER","NOVEMBER","DECEMBER"):
    print("fourth quarter")
else:
    print("plz enter a valid month")
