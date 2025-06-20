"""
Inheritance: mainly used for code -reusability , Avoid duplication
Acquiring the properties of attributies(variables) and behaviour(methods) from one class to another class is called inheritance
class A  --->a,b,c m1(),m2()--> A is the parent of B (super/parent class)
class B ---->x,y,z m3() ---> B is the child of parent class A( subclass /derived class)
Types of inheritance:
1.single -> 1parent->1 child
2.multiple ->parent1->parent2->child
3. multi level -> 1 parent->1 child->1child
4.Heirerkey ->1parent->child1->child2

covered topics:
inheritance types
super()
method overriding
"""

#Example1: single inheritance
class A:
    a,b=100,200
    def m1(self):
        print("m1 method from classA")
        print(self.a+self.b)

class B(A):        # b is child of parent class A
    x,y=200,100
    def m2(self):
        print("m2 method of classB")
        print(self.x-self.y)

obj1=B()
obj1.m1()  #m1 is the method of class A
obj1.m2()  #m2 is the method of class B

#Example2: Multilevel inheritance

class A:
    a,b=100,200
    def m1(self):
        print(self.a+self.b)

class B(A):        # b is child of parent class A
    x,y=200,100
    def m2(self):
        print(self.x-self.y)

class C(B):      # C is child of class B
    i,j=10,20
    def m3(self):
        print(self.i*self.j)
obj1=C()
obj1.m1()
obj1.m2()
obj1.m3()

#Example3: Hirarechy inheritance

class A:
    a,b=100,200
    def m1(self):
        print(self.a+self.b)

class B(A):        # b is child of parent class A
    x,y=200,100
    def m2(self):
        print(self.x-self.y)

class C(A):       #C is the child of parent A
    i,j=10,20
    def m3(self):
        print(self.i*self.j)
obj1=C()
obj1.m1()
obj1.m3()

#Example4: Multiple inheritance

class A:
    a,b=100,200
    def m1(self):
        print(self.a+self.b)

class B:
    x,y=200,100
    def m2(self):
        print(self.x-self.y)

class C(A,B):           #C is the child of classA and class B
    i,j=10,20
    def m3(self):
        print(self.i*self.j)
obj1=C()
obj1.m1()
obj1.m2()
obj1.m3()

#Example5: if 2 classes have same method name , then calling the parent class method using child class
class A:
    def m1(self):
        print("this is M1 method of class A")
class B(A):
    def m1(self):
        print("this is M2 method of class B")
        super().m1()    # super() function is used to invoke the parent class methods from child class

obj1=B()
obj1.m1()   #this is M2 method of class B
            #this is M1 method of class A

#Example6:
class A:
    a,b=10,20
class B(A):
    i,j=100,200
    def m(self,x,y):
        print(x+y) #local variables
        print(self.i+self.j) # Class variables
        print(self.a+self.b) # parent class variables are belongs to class B
obj1=B()
obj1.m(1000,2000)

#Example7: overriding the parent class A variables to child class B
class A:
    name="jyo"
class B(A):
    name="eshwar"    # method overriding of variables of class A
    def m(self):     # create new method to access the parent class variable value
        print(super().name)
obj1=B()
print(obj1.name)    #eshwar
obj1.m()    #jyo

#Example8: overriding methods,

class Bank:
    def rateOfInterest(self):
        return 0
class XBank(Bank):
    def rateOfInterest(self):
        return 10
class YBank(Bank):
    def rateOfInterest(self):
        return 12
obj1=XBank()
print(obj1.rateOfInterest())  #10

obj2=YBank()
print(obj2.rateOfInterest())  #12











