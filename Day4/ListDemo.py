'''
list is ordered and changable
list is mutable
len(mylist) -> to get length of list
mylist.append(),insert()-> to add itemes into another list
mylist.pop(),del.mylist[1] ,mylist.clear()-> to del the items
mylist.copy(),list(mylist)- to copy from one list to another
'''

#Example1: how to create list
mylist1 =[10,20,30]
mylist2 = ['Apple','Banana','orange','kiwi','pomo','avacado']
mylist3 =['apple',10,'banana']
mylist4=()

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist4)
print(type(mylist1))

#Example2: how to access the list
print(mylist1[0]) #index starts from zero
print(mylist2[-1])  # -1 index is starts from last element

#Example3: Range of indexes
print(mylist2[2:5])
print(mylist2[-1:-4])

#Example4: change item value
mylist2[2]="watermelon"
print(mylist2)

#Example5: reading elements using loop statement
for i in mylist2:
    print(i)

#Example6: check if item is exists in given list or not
mylist6 = ['Apple','Banana','orange','kiwi','pomo','avacado']

if "apple" in mylist6:
     print("Apple is present in list")
else:
    print("apple is not present in list")

#Example7: length of list
print(len(mylist6))  #6

#Example8: Add new item in list ->append(),insert()
mylist6.append('badam')  # new item will be added at end of list
print(mylist6)
mylist6.insert(3,"papaya") # it will insert new value some where in middle of list
print(mylist6)

#Example9: remove elements from list -> pop(), del, clear()
mylist6.pop(3)   #to delete using index
print(mylist6)

del mylist6[2]   #del is key used to delete items using index
print(mylist6)

mylist6.clear()   #clear() is used to remove all items from list
print(mylist6)

#Example10: copying one list into another list -> list(), copy()
mylist5=list(mylist2)
print(mylist5)

mylist1=mylist3.copy()
print(mylist1)

#Example11: combine /join lists
#1. using +operator
list1=['a','b','c']
list2=[1,2,3]
list3=list1+list2
print(list3)

#2. using loop statement
list4=['a','b','c']
list5=[1,2,3]
for i in list5:
    list4.append(i)
print(list4)

#3. using extend()
list1.extend(list2)
print(list1)







