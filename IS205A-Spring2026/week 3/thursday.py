print("hello") # need () to make it work
print # syntax we use elsewhere

# let's talk about () a bit more
print("hello", 1 + 10)

# the rules for () use, the arguments/parameters
# come from the function def itself
# sometimes it can work with nothing
print()
# sometimes some can take many-
print(1, 2, 3, 4, 5)
print("the thing is", 1) # should be 10000
# some have stricter rules
print(int(10.6666))
print(int()) # does have default behavior
# print(int("10.66666")) # too many hops
# print(int(10.666, 11.33)) # too many

# some are pretty strict about how many
print(round(10.66666)) # works with one
print(round(10.66666, 2)) # using that optional arg
# print(round(10.66666, 10.1132, 10.8558))
# print(round(10.5435, 10.424)) # gave it the wrong thing

# why might we define functions?
# for repetition (80% of the time)
# for cleaning up code a bit (20% of the time)

# how do we actually define a function?
# be careful about! spacing, indents, typos, punctuation

def name(paramater):
    # do your business whatever it is
    # ending up with a result
    result = "I did stuff!"
    return result # return the thing you want

##

# let's mak a basic greeting function
"""
1. name? greeting
2. inputs? one, a string, called name
3. the business? create a greeting
4. return? the greeting, a string
"""

def make_greeting(the_name):
    # make a greeting here
    greeting = "hello there, " + the_name
    # print(name) # allowable but only informational
    return greeting

# print(the_name) # outside can't see in
print(make_greeting("oliver"))
print(make_greeting("phillip"))
my_greeting = make_greeting("pero")
print(my_greeting)