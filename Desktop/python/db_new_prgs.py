# Reference url :
# http://www.oracle.com/technetwork/articles/dsl/python-091105.html
# Connecting to oracle database

import cx_Oracle
con = cx_Oracle.connect('scott/tiger')
print(con.version)
con.close()
#____________________________________________________
# Retrieving data from DB table using python for loop
import cx_Oracle
con = cx_Oracle.connect('scott/tiger')
cur = con.cursor()
cur.execute('select empno,ename,job,sal,deptno from emp')
print(type(cur))
for result in cur:
    print(result)
cur.close()
con.close()
#_______________________________________
Retrieving data from DB table using cx_Oracle module methods

import cx_Oracle
con = cx_Oracle.connect('scott/tiger')
cur = con.cursor()
cur.execute('select empno,ename,job,sal,deptno from emp')
'''
x=cur.fetchone()
print(x)
x=cur.fetchone()
print(x)
x=cur.fetchone()
---------------
x=cur.fetchmany(5)
print(x)
'''
x=cur.fetchall()
print(x)
print("Total no.of records : ",len(x))
cur.close()
con.close()
#_________________________________________________
#creatinga a table

import cx_Oracle
con = cx_Oracle.connect('scott/tiger')
cur = con.cursor()
cur.execute('create table student(sid number,sname varchar2(40),fee number,course varchar2(30))')
cur.close()
con.close() 
#____________________________________________
# inserting one record to db

import cx_Oracle
import os
con = cx_Oracle.connect('scott/tiger')
cur = con.cursor()
# Insert default rows
cur.execute("insert into student values(101,'Sai',6000,'python')")
con.commit()
cur.close()
con.close()
#_________________________________
#Inserting multiple records into table

import cx_Oracle
import os

con = cx_Oracle.connect('scott/tiger')
cur = con.cursor()
# Insert default rows
rows = [(101,'Ganesh',6000,'Python'), (102,'Lakshmi',1500,'Unix'),
        (103,'Vishnu',6000,'Shell'), (104,'Padma',1500,'AWS')]
cur.bindarraysize = 4
cur.setinputsizes(int, 30, int, 100)
cur.executemany("insert into student(sid, sname, fee, course) values (:1, :2, :3, :4)", rows)
con.commit()
cur.close()
#_____________________________________
#calling stroed procedure

import cx_Oracle
con = cx_Oracle.connect('scott/tiger')
cur = con.cursor()
myvar = cur.var(cx_Oracle.NUMBER)
cur.callproc('square', (200, myvar))
print(myvar.getvalue())
cur.close()
con.close()




