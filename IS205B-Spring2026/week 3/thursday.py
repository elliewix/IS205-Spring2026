# we've seen functions
print("hello")
# print will work empty
print() # prints an empty line
print("one argument")
print("one", "and another argument")
# there's a syntax thing that might confuse you

print(round) # valid but not what you wanted


# other functions that have different rules
# how round works
# print(round()) # doesn't work correctly
print(round(10.66765456543)) # works with 1
print(round(10.9876789, 3))

# common errors/problems
## give it the right number of args but
## not the right content
## related to, giving it mulitple values
## to act on, when it only wants to act on one

## I have a whole bunch of numbers to round
# print(round(18.445, 1948.34524, 10, 523.1))
# print(round(18.445, 10.34)) # 2nd arg can't use a float
# what if my second number met requirements?
print(round(190.4342, 100))
## just be careful about how you use them

# writing custom functions
## why?
## 80% to use repeatedly or in a repetition structure
## 20% to clean up code

## a few warnings
## there's a lot that's optional
## so if you forget, you won't get yelled at
## some concepts are weird/meta, you have to
## deal until other stuff better

# what's the actual template?

# first, answer the four questions
"""
1) what should the name be?
    - make_greeting
2) what parameters, if any to take?
    - name, as a string
3) what business to do?
    - create a nice greeting
4) what should it return?
    - return that greeting as a string
"""

def make_greeting(name):
    greeting = "hello there, " + name
    print(name) # use to get info within func, but just info
    return greeting #return always last line

# when return a value,you need to print the call
print(make_greeting("oliver"))
print(make_greeting("phillip"))
my_greeting = make_greeting("pero")
print(my_greeting)
# print(name)outside world can't see in
