"""
When we want to import the function from different package then we have to import sys
and then provide path of that package
"""
#Approach1
import sys
sys.path.append("C:/Users/Jyoshna/PycharmProjects/PythonProject/Day8/package1")
import module1
import module2

module1.display()
module2.show()

#Approch2:
import sys
sys.path.append("C:/Users/Jyoshna/PycharmProjects/PythonProject/Day8/package1")

from module1 import *
from module2 import *

display()
show()



