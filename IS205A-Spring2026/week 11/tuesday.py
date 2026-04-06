# dictionaries!
# our key/value pair friends

# creating an empty dict
data = {} # alt dict()

# we'll be treating dicts as
# a "collection of counters"

# why do we use dicts?

text = "hello fellow humans"

count_h = 0
count_e = 0
count_l = 0
count_space = 0
count_f = 0
# if I really wanted to the coding like this
for char in text:
    if char == "h":
        count_h = count_h + 1
    elif char == "e":
        count_e = count_e + 1
    elif char == "l":
        count_l = count_l + 1
    elif char == " ":
        count_space = count_space + 1
    # we're stopping here

print(count_h, count_e, count_l, count_space)
# so this solution is kind of terrible
# let's see how a dictionary will go about it

# to do so, we need to know some core
# dictionary syntax

example = {} # create an empty dict
# set a new key/value pair
example['key'] = 'value'
print(example)
# update an existing key/value pair
# note that this is the same!
# be careful
example['key'] = 'something else'
print(example)
# let's get some content out
print(example['key'])

# let's actually make the dictionary that
# we did on the board

# letters = {} # will hold the letter counts
# text = "hello fellow humans"
# for char in text:
#     letters[char] = 'found one'

letters = {} # will hold the letter counts
text = "hello fellow humans"
for char in text:
    # we need some logic
    if char in letters: # if the key is present
        # letters[char] = letters[char] + 1 # increment
        letters[char] += 1 # can use a stortcut
    else: # if it isn't in there
        letters[char] = 1 # create the pair
print(letters)

# alternatively, we can "prepopulate" a dictionary
# where we establish all the keys first with a base
# value, and then loop/increment

letters2 = {}
for char in text: # establishing loop
    letters2[char] = 0 # 0 because we don't want to count yet
print(letters2)
for char in text:
    letters2[char] += 1 # now we count
print(letters2)

# another version of prepopulation
# you have a larger set of data
# but you're observing a subset
import string
letters3 = {}
for char in string.ascii_letters + string.punctuation + " ":
    # prepopulate with the full set
    letters3[char] = 0
for char in text:
    letters3[char] += 1

print(letters3)

# a shorter way to handle things

letters4 = {}
for char in text:
    letters4[char] = letters4.get(char, 0) + 1

print(letters4)

