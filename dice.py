from specialInput import *
#! /usr/bin/env python
import random
sides=int_input("How many sides the die should have?")
while sides<2:
    sides=int_input("The sides should have at least 2 sides, how many sides?")
dice=int_input("How many dice?")
for roll in range(1,dice):
    print random.randint(1,sides)
