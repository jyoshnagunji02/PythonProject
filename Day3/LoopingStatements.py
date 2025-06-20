"""
we will use all looping functions along with the range() function
range(10)  o/p: [0,1,2,3,4,5,6,7,8,9
range(1,10) o/p: 1,2,3,4,5,6,7,8,9
range(1,10,2) o/p: 1 to 9 incremented by 2 = 1,3,5,7,9
to print the range we have to use list(range(10) o/p: [0,1,2,3,4,5,6,7,8,9]

looping statements:
while loop :
initialization, condition, incrementation
for loop:
use range() function

"""

print(list(range(10)))
print(list(range(1,10)))
print(list(range(1,10,2)))
print(list(range(5,10)))

#to print only odd numbers between 1 to 20
print(list(range(1,20,2)))

#to print only even numbers between 1 to 20
print(list(range(2,20,2)))

# to print 1 to 10 in descending order
print(list(range(10,1,-1)))

print(list(range(-10,-5)))  #-10.-9,-8,-7,-6

print(list(range(-10,-5,2)))  #-10,-8,-6

#Example: print 1..........10 numbers
#While loop
i=1
while i<=10:
    print(i)
    i=i+1
print("While loop Done!!!")
#For loop
for i in range(1,11):
    print(i)
print("For Loop Done")

#Example: print 1.......10 numbers in descending order
#While loop
i=10
while i>=1:
    print(i)
    i=i-1
print("Descending order done!!!")
#For loop
for i in range(10,0,-1):
    print(i)
print("For Loop Descending order Done")

#Example: print only even numbers between 1 to 20
for i in range(2,20,2):
    print(i)
print("even numbers are printed")

#print 5,10,15,20....100
for i in range(5,101,5):
    print(i)

#how to print multiples of 6
for i in range (6,61,6):
    print(i)














