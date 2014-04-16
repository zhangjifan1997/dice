from specialInput import *
#! /usr/bin/env python
import random
sides=int_input("How many sides the die should have?")
dice=int_input("How many dice?")
for roll in range(1,dice):
    print random.randint(1,sides)
