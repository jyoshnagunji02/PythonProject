'''
import the function from 2 different packages
'''
#Approch1:
import  sys
sys.path.append("C:/Users/Jyoshna/PycharmProjects/PythonProject/Day8/pack1")
sys.path.append("C:/Users/Jyoshna/PycharmProjects/PythonProject/Day8/pack1/pack2")

import module1
import module2
module1.display()
module2.show()

#Approach2:

import  sys
sys.path.append("C:/Users/Jyoshna/PycharmProjects/PythonProject/Day8/pack1")
sys.path.append("C:/Users/Jyoshna/PycharmProjects/PythonProject/Day8/pack1/pack2")

from module1 import *
from module2 import *

display()
show()


