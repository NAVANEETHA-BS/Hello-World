'''
def   f1() :
    print("I am local f1")

class  Sample :
    def  f1(self) :
        print("I am f1")
    def  f2(self) :
        print("I am f2")
    def  f3(self) :
        f1() # I am local f1
        self.f1() # I am f1
        self.f2()
        print("I am f3")

x=Sample()
x.f3()
f1()


class   Sample :
    __a=100
    b=200

    def   __f1(self) :
        print("I am private f1 function")
        
    def   f2(self) :
        print(" I am public f2,calling private f1")
        self.__f1()
        print("a=",Sample.__a)

x=Sample()
#print(x.__a)
#x.__f1()
x.f2()
print("b=",Sample.b)
'''


class  A :
    
    def __init__(self) :
       print("Hey, I am a constructor")
        
    def  f1(self) :
       print("I am f1")
     

a=A()
b=A()
c=A()
a.f1()





























