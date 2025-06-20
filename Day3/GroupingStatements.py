'''
Jumping Statements:
break, continue
'''

#Example1:
for i in range(1,10):
    if i==5:
        break
    print(i)
print("break is working")  #o/p: 1,2,3,4


#Example2:
for i in range(1,10):
    if i==4 or i==7:
        continue
    print(i)
print("continue is worked")


