stats=[['01/02/2019','south africa','not out','virat kohli',342],
       ['01/02/2019','south africa','bowled','virat kohli',242],
       ['21/08/2019','australia','catch','virat kohli',289],
       ['01/02/2019','south africa','not out','virat kohli',323],
       ['18/04/2019','india','not out','virat kohli',275],
       ['01/02/2019','south africa','not out','virat kohli',198]]

'''
#number of not_outs based on monthwise
x={}
months=set([i[0].split("/")[1] for i in stats])
#print(months)
for j in months:
    cnt=0
    for i in stats:
        m1=i[0].split("/")[1]
        if i[2]=="not out" and j==m1:
            cnt+=1
    x[j]=cnt
print(x)
'''

#countrywise,monthwise, calculate total runs and average runs
'''
countries=set([i[1] for i in stats])
months=set([i[0].split("/")[1] for i in stats])
#print(months)
#print(countries)
for i in countries:
    x={}
    for j in months:
        total_runs=0
        cnt=0
        list1=[]
        d1={}
        for k in stats:
            cntry=k[1]
            mm=k[0].split("/")[1]
            if cntry==i and j==mm:
                total_runs+=k[4]
                cnt=cnt+1
        if total_runs!=0:
            avg_runs=total_runs/cnt
            list1.append([total_runs,avg_runs])
            d1[j]=list1
            #print(d1)
            x[i]=d1
            print(x)
'''

stats=[['01/02/2019','south africa','not out','virat kohli',342],
       ['01/02/2019','south africa','bowled','virat kohli',242],
       ['21/08/2019','australia','catch','virat kohli',289],
       ['01/02/2019','south africa','not out','virat kohli',323],
       ['18/04/2019','india','not out','virat kohli',275],
       ['01/02/2019','south africa','not out','virat kohli',198]]

countries=set([i[1] for i in stats])
months=set([i[0].split("/")[1] for i in stats])
print(countries)
print(months)
for i in months:
    x1={}
    for j in countries:
        d={}
        l=[]
        sum1=0
        cnt=0
        for n in stats:
            cnty=n[1]
            mm=n[0].split("/")[1]
            
            if j==cnty and i==mm:
                sum1=sum1+n[4]
                cnt+=1
                
        if sum1!=0:
            avg=sum1/cnt
            l.append([sum1,avg])
            d[j]=l
            #print(d)
            x1[i]=d
            print(x1)
                
            
                
                
                




























            
                      












