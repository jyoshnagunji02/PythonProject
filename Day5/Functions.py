'''
Function means set of statement which will perform task
1.function creation
2. invoke the function
'''
#Example1:
def myfunc():
    print("created customised function")
myfunc()

#Example2:
def myfunc(name):
    print("my arg func",name)
myfunc("jyo")

#Example3:
def myfunc(a,b):
    return(a+b)
sum=myfunc(10,20)
print(sum)

#Example4:
def fun():
    return
fun()  # returns none

def myfunc1():
    i=10
myfunc1()  #this also return none

#Example5:
def myfunc2(a,b):
    print(a+b)     # here if we add return then output should be assigned to varaiable and then print that
myfunc2(20,30)







