'''
1. positional arguments
2.Keyword arguments

always positional arguments should be declared before passing keyword arguments
RETURN TYPE OF FUNCTION IS tuple
'''
#Example1
def my_fun(i,j):    #positional arguments
    print(i,j)
my_fun(10,20)
my_fun(i=30,j=40)  #keyword arguments

#Example2:values assigned to positional arguments
def myfunc(i,j=10):
    print(i,j)
myfunc(20)
myfunc(100,200)   #100,200 , it will replace the default value

#Example3: Keyword arguments
def greeting(name,greetmsg):
    print(greetmsg+" "+name)
greeting(name='john',greetmsg='hello')
greeting(greetmsg='hello',name='john')  #hello john

#Example4:
def func(a,b,c):
    print (a,b,c)
func(10,20,30)  #10,20,30
func(10,20,c=50)  #10,20,50
#func(10,b=30,20)  # it is not allowed
func(10,b=30,c=70) #10,30,70

#Example5:
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(largest(20,30)) #30,20
print(largest(30,20))  #30,20

res=largest(10,50)
print(res)    #return type is TUPLE



