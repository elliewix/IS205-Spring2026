# let's make a function together
"""
1. name? split_bill
2. inputs? the bill amount (bill), the proportion (my_prop)
3. what to do? calculate the share
4. return? the calculation amount
Write a function that calculates your share of
a bill given a proportion. Return the calculated amount.
Example: $100, 20% should be $20
example call: split_bill(100, .2) result 20
"""

def split_bill(bill, my_prop):
    # this is where I do things
    total = bill * my_prop
    return total

# print(split_bill(100, .2)) # 20
my_total = split_bill(100.3456, .9876534)
print(my_total)
print(round(my_total, 2))

# switching gears
# importing functions
## your default way of importing modules
import random
print(random.randint(0,10))

## import as an alias only if community style req
import random as rd
print(rd.randint(0,10))

## only use these in really specific situations
## none of which will be in 205

## import the functions into the primary namespace
from random import randint
# let's me use it but nothing else from that module
print(randint(0, 10))

# import everything into the namespace
from random import * # the most dangerous one
print(choice([0,8,76,7,9]))

