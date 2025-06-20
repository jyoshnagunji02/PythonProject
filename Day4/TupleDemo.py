'''
Tuple is ordered and un changable
Tuple is represented by ()
tuple is immutable
immutable means we cannot change its value
1. modifying existing tuple is not possible
2. removing the elements is not possible
3. we cannot append the new value
4. we cannot insert the new value
'''

#Example1: creating the tuple
myTuple= ('apple','banana','kiwi')
print(myTuple)

#Example2: Accessing the items in tuple
myTuple1=('apple',10,'kiwi',1,4,56)
print(myTuple1[2])
print(myTuple1[-1])

#Example3: Range of indexes
print(myTuple1[1:4])
print(myTuple1[-4:-1])

#Example4: changing the tuple items
#by default tuple does not allow you to change values because it is immutable
#convert tuple to list and then to tuple

mylist =list(myTuple1)
mylist[0]='papaya'
myTuple2=tuple(mylist)
print(myTuple2)

#Example5: coping one tupple into another
myTuple3=myTuple2
print(myTuple3)

#Example6: del tuple
#del myTuple3
#print(myTuple3) # error

#Example7: joining/combining

tuple1=myTuple1+myTuple2
print(tuple1)



