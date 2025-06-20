'''
Global varaibles: varaibles which are created outside of function,
it can be accessed any where inside /outside function
Local Varaibles: variables which are created inside of function
'''

#Example1:

global_var=20
def myfun():
    local_var=10 #intendataion
    print(local_var)
    print(global_var)
myfun()

#Example2: if varaibles names are same then inside func it will consider local variable only

xy=100       #global variable
def cool():
    xy=200    #local variable
    print(xy)
cool()

#Example3:
xy =100
def cool1():
    global xy   # declare variable as global and the update the value of global variable and print that
    xy=300
    print(xy)  #300
cool1()
print(xy)   #300

#Example4:
x =100
def cool2():
    global x  # declare variable as global and the update the value of global variable and print that
    x=300
    print(x)  #300
#cool2()
print(x)  #100

#Example5: if we want to create global varaibles inside func but we have to specify with global keyword

def cool3():
    global y  # declare variable as global and the update the value of global variable and print that
    y=300
    print(y)
cool3() #300
print(y) #300   #able to access global varaible outside of func also

