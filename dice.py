#! /usr/bin/env python
from specialInput import *
import random
dice=int_input("How many dice?")
for roll in range(0,dice):
    sides=int_input("How many sides the die should have?")
    while sides<2:
        sides=int_input("The die should have at least 2 sides, how many sides?")
    print random.randint(1,sides)
