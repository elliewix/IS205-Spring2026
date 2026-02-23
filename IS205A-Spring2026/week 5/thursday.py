import string

print(string.punctuation)

for punc in string.punctuation:
    print(punc)

###
def greeting(name):
    # our function will get the content from name
    # when you call the func and pass it content
    return "hello " + name

person1 = "Elizabeth"
cat1 = "Phillip"
cat2 = "Oliver"
print(greeting(person1))
print(greeting(cat1))
print(greeting(cat2))
# WE ARE NOT DOING greeting(person1, cat1, cat2) etc...

# looking at the in keyword again....

text = "I have project."
print("project" in text) # True
# in with a string looks for substrings
split_text = text.split()
print(split_text)
print("project" in split_text) # False
# in with a list looks for exact membership
clean_text = text.replace('.', '') # cleans out .
clean_split = clean_text.split()
print(clean_split)
print("project" in clean_split) # True

# defining two functions and one uses the other
def greeting(name):
    # our function will get the content from name
    # when you call the func and pass it content
    name = format_name(name)
    return "hello " + name

def format_name(name):
    name = name.title()
    return name

person1 = "elizabeth"
cat1 = "phillip"
cat2 = "oliver the deep coward"
print(greeting(person1))
print(greeting(cat2))
print(greeting("phillip the bold"))