'''
Set - it is unordered and unindexed and it is represented by curly braces
Set is mutable

add() -> add single element
update() -> add multiple items in set
remove items from set :
remove()-> when we try to remove non existing items using remove(), then it gives error
discard()-> when we try to remove non existing items using remove(), then it wont give any error
clear()-> to remove all items
del -> to remove along with empty sets
union(),update()-> to join two sets

'''
#Example1: creating set
myset1= {'apple','banana','kiwi'}
print(myset1)

#Example2: Accessing the items in set
for i in myset1:
    print(i)

#Example3: Value exists in set or not
if 'banana' in myset1:
    print("item present in set")
else:
    print("item not present in set")

#Example4: Adding items to set
#add()-> add only single element to set
myset1.add("papaya")
print(myset1)
#update()-> used to add multiple values in set
myset1.update(["mango","gouva"])
print(myset1)

#Example5: find number of items in set
print(len(myset1))

#Example6: remove the elements in set->remove(),discard()
myset1.remove('banana')
print(myset1)

myset1.discard("mango")
print(myset1)

#Example7: remove all values from set -> claer(),del
myset1.clear()
print(myset1)  #it will print empty set , o/p: set()

#del myset1
#print(myset1) #NameError: name 'myset1' is not defined

#Example8: joining 2 sets -union(),update()
mySet2={10,20,30}
mySet3={"apple","banana","kiwi"}
mySet=mySet2.union(mySet3)
print(mySet)

mySet4={10,20,30}
mySet5={"apple","banana","kiwi"}
mySet4.update(mySet5)
print(mySet4)


