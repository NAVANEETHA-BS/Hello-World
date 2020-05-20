'''
#1)write a program to find area of the circle(area=pi*r*r)
#area of circle=pi*r*r
#pi=3.14

radius=float(input("enter radius : "))
pi=3.14
areaOfCircle=pi*radius*radius
print("area of the circle %0.2f " %(areaOfCircle))


#2)write a program to find area of the triangle(area=1/2*b*h)

base=float(input("enter base : "))
height=float(input("enter height : "))
areaOfTriangle=1/2*base*height
print("area of the triangle %0.2f" %(areaOfTriangle))



#3)write a program to find the area of the square

side=float(input("enter side : "))
areaOfSquare=side*side
print("area of the square %0.2f" %(areaOfSquare))



#4)write a program to find area of the rectangle(breadth*height)

breadth=float(input("enter breadth : "))
height=float(input("enter height : "))
areaOfRectangle=breadth*height
print("area of rectangle %0.2f" %(areaOfRectangle))



#6)write a program to find the square root  of the given number

n=int(input("enter a number : "))
sqrRoot=n**(1/2)
print("square root of %d is %0.2f" %(n,sqrRoot))



#5)write a program to find square and cube of the given number

n=int(input("enter a number : "))
square=n**2
cube=n**3
print("square of the given number of %d is %0.2f" %(n,square))
print("cube of the given number %d is %0.2f" %(n,cube))


#7)write a program to accept centimeters and convert into meters and kilometers

centimeter=float(input("enter number of centimeters : "))
meters=centimeter/100
kilometers=centimeter/1000
print("%0.2f centimeters= %0.2f meters" %(centimeter,meters))
print("%0.2f centimeters=%0.2f kilometers" %(centimeter,kilometers))



#8)write a program to accept celsius temperature and convert into fahrenheit
# celsius to fahrenheit: ('c*9/5)+32='f
#fahrenheit to celsius: ('f-32)*5/9='c




######if assignments

#7)wap accept a character and check the character is alphabet or not

ch=input("enter a character : ")
if (ord(ch)>=65 and ord(ch)<=90) or (ord(ch)>=97 and ord(ch)<=122):
    print(ch,"is a character")
else:
    print(ch,"not a character")



ch=input("enter a character : ")
if ch.isalpha():
    print(ch,"is a character")
else:
    print(ch,"is not a character")



x=input("enter any string : ")#banana
d1={}
for i in x:
    d1[i]=x.count(i)
    print(d1)

    #for i,j in d1.items():
        #print((i,j))
        #for j in d1:
           # print(j)
    

values=sorted(d1.values())
print(max(values))
 '''

x=input("enter any string : ")
d1={}
for i in x:
    d1[i]=x.count(i)
    print(d1)
x=d1.items()
print(x)
for j,k in d1.items():
    print(j,k)
    
values=sorted(d1.values())
print(max(values))
    





























    

































