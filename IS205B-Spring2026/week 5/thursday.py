import string

print(string.punctuation)
print(len(string.punctuation))

for punc in string.punctuation:
    print(punc)

## so thinking about the detect word function

text = "I have a cat"
# in checks substrings on a string
print("cat" in text) # True
print("at" in text) # True
# what if we wanted "at" to be false?

split_string = text.split()
# in checks for exact equality when looking at a list
print(split_string)
print("cat" in split_string) # True
print("at" in split_string) # False

text = "I have a cat."
split_string = text.split()
print(split_string)
print("cat" in split_string)

text = "I have a cat."
text = text.replace(".", "")
clean_split = text.split()
print(clean_split, "cat" in clean_split)

# let's think about functions now

def greeting(name):
    text = "hello " + name
    return text

person1 = "elizabeth"
cat1 = "phillip"
cat2 = "oliver"
print(greeting(cat1))
print(greeting(cat2))
print(greeting("oliver the coward"))

def format_name(name): # imperfect because names are complex
    text = name.title()
    return text

print(format_name(cat1))
print(format_name(cat2))
print(format_name("oliver the coward"))

def greeting(name):
    text = "hello " + format_name(name)
    return text

print(greeting("oliver the coward"))
print(greeting("phillip the bold"))