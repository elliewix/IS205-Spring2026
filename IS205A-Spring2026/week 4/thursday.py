# in keyword and strings
# will check for substrings
print("cats")
print("cat" in "cats")
print("hell" in "hello")

# there are also boolean methods
print("12345234".isnumeric())

# what do we do with these??
# we use it in if statements!
text = "2349829"
print(text.isnumeric())
# when we want to take an action based
# on the results of those boolean exps
# we use an  if block
## if boolean:
##     do stuff if true
text = "2349829 cats"
print(text)
if text.isnumeric() == True:
    print("the text is numerical!")
# nothing will happen when false
text = "2349829 cats"
if text.isnumeric():
    print("text is numeric")
else:
    print("text has non numeric stuff")