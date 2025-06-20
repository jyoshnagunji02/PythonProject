""" Control Statements
1. conditional statements
2. looping statements
3. jumping statements

"""
#contional statement
#Example1: print person is eligible to vote
age=int(input("enter the age input: "))
if age>=18:
    print("eligible to vote")   #intendation space
else:
    print("not eleigible to vote")

#example2

if True:
    print("true condition")
else:
    print("false condition")


#Example3

if 1:               #here 1 represents true , 0 represents false
    print("true")
    print("mutiple true values")
else:
    print("false")
    print("multiple false values")


#Example4 verify given number is even or odd

num=int(input("enter number"))
if(num%2==0):
    print("even number")
else:
    print("odd number")

#if else in single statement
num =11
print("even number") if (num%2==0) else print("odd number")

#mutiple printstatements
a=23
{print("hello"),print("python")} if a>=10 else {print("hi"),print("java")}

#example5 : multiple conditions using elif
weekno=1
if weekno==1:
    print("sunday")
elif weekno==2:
    print("monday")
elif weekno==3:
    print("tuesday")
else:
    print("invalid weekno")




