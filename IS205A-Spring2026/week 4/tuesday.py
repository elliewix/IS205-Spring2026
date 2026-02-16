# let's write a function together
"""
1. name? split_bill
2. inputs? bill, your portion (my_prop)
3. do? calculates your portion of a bill
4. return? the calculated amount
"""

# test example
# a bill of $100 and you pay 20% should be $20
# so the example call would be split_bill(100, .2)

def split_bill(bill, my_prop):
    total_share = bill * my_prop
    return total_share

# print(split_bill(100.34, .2))
total = split_bill(100, .234455)
print(round(total, 2))

# importing functions
## your default way of doing this
import random
## you have to say random.functionname...
print(random.randint(0,10))
## when the community has a certain style, you follow that
# import pandas as pd
# import numpy as np
import random as rd # don't do this, just an example
## you can use stuff like
print(rd.randint(0,10))

# those are your two main ways of importing modules
# the others below and ONLY to be used for specific situations
## import just a specific function into the built in namespace
from random import randint
print(randint(0,10))
## or all the things, into your full namespace
from random import *
print(choice([0,9,8,8]))

###

# booleans and logic!
## at the core we have boolean expressions
print(True, False)
## boolean operators, any operator that results in a bool
## all your usual math things
print(5 == 5) # == is equality
print(5 != 5) # not equal to
print(5 > 5) # greater than, False
print(5 >= 5) # greater than or equal, True

# boolean keywords
## for 205, (is, not) are both banned
## but we will use in a bunch
print("a" in "cat")

