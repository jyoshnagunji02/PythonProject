"""
Method:
method is written with any name and it returns value
method can accepts arguments /parameters
we have to create object to invoke the method

Constructor:
it is written as  __init__(self)
it does not return any values
constructor is invoked at the time of object creation
"""
#Example1: default constructor
class myclass():
    def __init__(self):
        print("this is constructor..")
    def m1(self):
        print("this is instance method..")
    def m2(self,x,y):
        return x,y

obj1=myclass()  #this is constructor..
obj1.m1()  #this is instance method
res=obj1.m2(10,20)
print(res)    #return type of function is tuple

#Example2: parameterised constructor
class myclass1():
    def __init__(self,name):
        print(name)
mc=myclass1("jyoshna")

#Example3: Create employee class, and pass the eid,ename,esal through constructor and display using display method

class myEmployee():
    def __init__(self,eid,eName,eSal):
        self.eid=eid
        self.eName=eName
        self.eSal=eSal
    def display(self):
        print(self.eid,self.eName,self.eSal)
mc1=myEmployee(10,'john',10000)
mc2=myEmployee(102,'jyos',3000)
mc1.display()
mc2.display()

#Example4: constructor that can return the only string value
class myEmp():
    def __init__(self,eid,eName,eSal):
        self.eid = eid
        self.eName = eName
        self.eSal = eSal
    def __str__(self):
        return (self.eName)   #return is mandatory
obj1=myEmp(10,'jyo',100000)
print(obj1)

