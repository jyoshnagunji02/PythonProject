'''
Dictionary is unordered and changable and indexed, it is represented in curly braces
Dictionary is mutable and stored as key and value paires
copy()
pop(),del,clear()
'''
#Example1: declaring the dict
mydic1={101:'x',102:'y',103:'z'}
print(mydic1)

#Example2: Accessing the values from dict-> using keys, get()
mydic2= {
    "jyo":10,
    "eshwar":20,
    "prathyu":30,
    "mahesh":40
}
print(mydic2['jyo'])

#using get()
print(mydic2.get("jyo"))

#Example3: change values from dict
mydic2["jyo"]=50
print(mydic2)

#Example4: Reading items from dict using loop

for i in mydic2:   # it prints only keys from dict
     print(i)

for i in mydic2:   # it prints only values from dict
     print(mydic2[i])

for i in mydic2.values():
    print(i)

for x,y in mydic2.items():  # to display all the items from dict
    print(x,y)

#Example5: check if item exists
if "jyoshna" in mydic2:
    print("exists")
else:
    print("not exists")

print("jyoshn" in mydic2)  # returns true or false

#Example6: add items in dict
mydic2["ramu"]=60
print(mydic2)

#Example7: Removing items from dict
mydic2.pop("ramu")
print(mydic2)

del mydic2["jyo"]
print(mydic2)

#del mydic2  # to del entire dict along with empty dict

mydic1.clear() # del entire dict but it contains empty dict
print(mydic1)

#Example8: copying the one dict to another
mydict3={
    "jyo": 10,
    "eshwar": 20,
    "prathyu": 30,
    "mahesh": 40
}
#without using copy()
mydict4=mydict3
print(mydict4)

#with copy()
mydict5=mydict3.copy()
print(mydict5)


