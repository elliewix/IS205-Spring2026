# Python booleans
print(True, False)
# we usually don't type these in
# we use code, boolean expressions, to
# produce True and False
# bool exps are any python code that
# returns/results in True or False
# some combo of boolean operators,
# boolean methods, or boolean keywords

# boolean operators
# punctuation that produces True/False
# ==, != not equal to, >, <, <=, >= etc.
# all the math things
print(5 == 5) # True
print(5 != 5) # False
print(5 > 5) # False
print(5 >= 5) # True

# boolean keywords
## the in keyword
# when given (content) in (content)
# it will check membership
# versus, for (thing) in (thing)
# which is a loop

# when in is doing membership....
# (content) in (a string)
# it will check substring matching
print("cat" in "cats") # True
print("dog" in "cats") # False
print("at" in "cats") # True
print("hell" in "hello")

# boolean methods

# a brief aside
poop = "💩"
print(poop)

##

# boolean methods
text = "1234234"
print(text.isnumeric())
name = "elizabeth"
print(name.capitalize())

# why do we care so much about TrueFase?
# to make if statements
# if ___boolean expression here___:
#    # when that's true do this stuff

text = "12342342354 cats"
if text.isnumeric() == True:
    print("yes this is all numeric")

# if it is false, nothing happens
text = "12342342354 cats"
if text.isnumeric() == True:
    print("yes this is all numeric")
else:
    print("not all numeric")