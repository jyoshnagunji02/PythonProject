#Approch1: if 2 modules having same functions with same name , then how to import to third module
import animal

animal.animal()
animal.bird()

import bird
bird.animal()
bird.bird()

#Apporch2: 

from animal import animal,bird
animal()
bird()

from bird import animal,bird
animal()
bird()