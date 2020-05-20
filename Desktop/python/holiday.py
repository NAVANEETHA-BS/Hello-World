from datetime import datetime, timedelta
#print(datetime.now() + timedelta(1))

def case_days(from_date, days):
    cnt = 0
    x = ["2020-03-03", "2020-03-04", "2020-03-05", "2020-03-06"]
    print(from_date)
    print(days)
    from_date = datetime.strptime(from_date, '%Y-%m-%d').date()
    print(from_date)
    to_date = from_date + timedelta(days)
    print(to_date)  # 2020-03-11
    print(x)
    for i in x:
        dates_list = datetime.strptime(i, '%Y-%m-%d').date()
        print(dates_list)
        if not from_date<dates_list<to_date:
            total = days
            
        else:
            
            cnt+=1
            print(cnt)
            to_date = datetime.strftime(to_date, '%Y-%m-%d')
            total = cnt + case_days(to_date, cnt)
    return total
    


y = case_days("2020-03-01", 10)
print(y)
# x = ["2020-03-03", "2020-03-04", "2020-03-05", "2020-03-06"]

# date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
