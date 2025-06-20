"""
Polymorphism  -> ability of method to do in multiple forms
it can be acheived using method overloading(same method in mutiple parameters) in same class
in python it is not acheived completely as like java, but there is different way to acheive it

"""
#Example1:
class A():
    def m1(self,name =None):
        if name is not None:
            print("hello "+name)
        else:
            print("No name")
obj1=A()
obj1.m1("jyo")
obj1.m1()

#Example2:
class A():
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
obj1=A()
obj1.add()
obj1.add(10,20)
obj1.add(20,30,40)
