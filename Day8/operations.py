#Approch1: calling functions from one file to another file
import caluclator
caluclator.add(100,200)
caluclator.add(10,20)

#Approch2:  to call specific functions
from caluclator import add,mul
add(10,20)
mul(20,30)

#Approch3: to call all functions
from caluclator import *
add(10,20)
mul(20,30)