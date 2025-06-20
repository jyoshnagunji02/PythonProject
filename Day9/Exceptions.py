"""
Exception is an event which will cause program termination
syntax
------
try:
  condition
except:
   condition
"""
#Exception1:
print("This is start of program")
try:
   print(x)
except:
    print("Exception is handled")
print("This is end of program")

#Example2:

print("second program started")
try:
    print(10/0)       # if exception occurs then only except block will execute
except ZeroDivisionError:
    print("Exception occured --Handled")
print("second program completed")

#Example3: Multiple except blocks -->try,except,else,finally
"""
except->Executes only when exception occurs
else->executes only when no exception is occured
finally : it is executed even though exception is occured or not

"""

try:
 num1,num2=10,0
 res=num1/num2
 print("result is :",res)
except ZeroDivisionError:
    print("thrown ZeroDivisonError")
except SyntaxError:
    print("thrown syntax error")
else:
    print("No Exceptions Occured")
finally:
    print("Always Execute:...")


#Example4: Raising our own exceptions
def engage(num):
    if num<0:
        raise ValueError("only integers are allowed")
    if num%2==0:
        print("even number")
    else:
        print("odd number")
try:
   num=-1
   engage(num)
except ValueError:
    print("Exception Handled...")
print("program execution completed")





