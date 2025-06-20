#Approach1  : invoke the other classes from other modules to different module
import a
import b

obj1=a.Animal()
obj1.display()

obj2=b.Bird()
obj2.display()

#Approach2:
from a import Animal
from b import Bird

obj1=Animal()
obj1.display()

obj2=Bird()
obj2.display()


