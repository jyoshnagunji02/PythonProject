'''

Python = Structured + object oriented language
Oops concepts:
class
object
inheritance
polymorphism(method overloading)

class:  collection of attributes(variables) and behaviour(methods)
it is blue print
logical entity
it does not occupy any space in memory

Object:
it is instance of class
physical entity
it occupies space in memory

once class can contain multiple objects and each object is independent

Function vs method:
------------------------
function: which is written outside of class
method: function which is written inside of class

covered concepts:
1. class, objects
2. static, instance methods
3. global,class,local variables
4. Functions(instance methods)


'''
#example1
class myclass:
    def func(self):     #by default for method inside class ,self is default argument we have to pass
        pass
    def newFunc(self):
        print("jyoshna")
    def display(self,name):  #passing arguments to a method
        print(name)
m1=myclass()           #declaration of object for the class
m1.func()              # no value will be printed as we dont print any value
m1.newFunc()           #jyoshna
m1.display("eshwar")   #eshwar

#Example2 # static method
'''
1. When we declare the instance method then self refers to class
2. when we declare static method self refers to static method only and when we want to call static method
we have to pass value to self argument also for static method
3. static method can me called by classname /by using object
'''
class myclass1:
    def func1(self):
        print("this is instance method....")
    @staticmethod
    def func2(self,num):
        print(self,num)
mc=myclass1()
mc.func1()
mc.func2(100,200)   #100,200  # calling static method using object
myclass1.func2(10,20)  # calling the static method using class name


#Example3: Class variables
"""
if we want to use class variables inside the method, we have to call using self
"""
class myclass2:
    a,b=10,20    # class variables
    def add(self):
        print(self.a+self.b)
mc=myclass2()
mc.add()

#Example4: Global variables,Class variables, local variables

i,j=10,20  #global variables
class myclass3:
    a,b=20,30   # class variables
    def addValue(self,x,y):   #local variables
        print(x+y)
        print(self.a+self.b)
        print(i+j)

mc=myclass3()
mc.addValue(11,20)

#Example5: global ,class ,local variables are same , then how to access the global variables?

a,b=10,20
class myClass4:
    a,b=20,30
    def addValue1(self, a, b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])
mc=myClass4()
mc.addValue1(11,22)

#Example6: Multiple objects for one single calss

class myclass5:
    def display(self,name):
        print("this is display method")
        print(name)
obj1=myclass5()
obj1.display("jyoshna")

obj2=myclass5()
obj2.display("eshwar")










































