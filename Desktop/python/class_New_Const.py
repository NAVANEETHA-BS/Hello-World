Constructor :
    
It is a special method of a class,It executes
automatically whenever object is created and it allocates
memory for given object.

The name of the constructor is :
def --init--(self,<arg1>,.....) :

Destructor :

It is also a special method of a class, It executes
automatically whenever the control is outside of the object
and it deallocates memory for object.

The name of the destructor is :
def --del--(self) :

#________________________________
#example of constructor

class  A :
    i=0
    def __init__(self) :
       A.i=A.i+1 
      
    def  f1(self) :
       pass
       

a=A()
b=A()
c=A()


print("Views : ",A.i)

#___________________________
# Example of parameterised construtctor
class  Student :
    cnt=0
    def __init__(self,name,course,fee) :
        self.name=name  # Insatnce variable
        self.course=course
        self.fee=fee
        Student.cnt+=1
    def  display(self) :
        print(self.name,",",self.course,",",self.fee)


a=Student("Ganesh","Python",3000)
b=Student("Hari","Unix",2500)
c=Student("Padma","Oracle",2800)


a.display()
b.display()
c.display()
print("Total no.of students : ",Student.cnt)
#____________________________________
# Example of parameterised construtctor
# Writing objects data to db table

import cx_Oracle
class  Student :
    cnt=0
    def __init__(self,name,course,fee) :
        self.name=name  # Insatnce variable
        self.course=course
        self.fee=fee
        Student.cnt+=1
    def  display(self) :
        print(self.__dict__)


con = cx_Oracle.connect('scott/tiger')
cur = con.cursor()

ans="y"
while ans in "Yy" :
    sname=input("Enter student name : ")
    course=input("Enter course name : ")
    fee=float(input("Enter fee : "))
    a=Student(sname,course,fee)
    a.display()
    l1=[[sname,course,fee]]
    cur.bindarraysize = 1
    cur.setinputsizes(30,30,int)
    cur.executemany("insert into student(sname,course,fee)values(:1,:2,:3)",l1)
    print("Inserted into DB table.")
    con.commit()
    ans=input("Do you want to register [y/n]:")
print("Total no.of students : ",Student.cnt)

cur.close()
con.close()
    
#_____________________________________________

# Example of parameterised construtctor
# Writing objects data to the file
class  Student :
    cnt=0
    def __init__(self,name,course,fee) :
        self.name=name  # Insatnce variable
        self.course=course
        self.fee=fee
        Student.cnt+=1
    def  write_to_file(self) :
       rec=str(Student.cnt)+","+self.name+","+self.course+","+str(self.fee)+"\n"
       x.write(rec)

x=open("student.txt","a")
while True :
    ans=input("Do you want to register(y/n) :")
    if ans in "Yy" :
        sname=input("Student name : ")
        course=input("Course name  : ")
        fee=float(input("Fee : "))
        a=Student(sname,course,fee)
        a.write_to_file()
    else :
        break
x.close()
    
#_________________________________________

    
