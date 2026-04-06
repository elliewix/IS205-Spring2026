text = "hello fellow humans"

count_h = 0
count_e = 0
count_l = 0
count_o = 0
count_space = 0
for char in text:
    if char == "h":
        count_h = count_h + 1
    elif char == "e":
        count_e = count_e + 1
    elif char == "l":
        count_l = count_l + 1
    elif char == "o":
        count_o == count_o + 1
    elif char == " ":
        count_space = count_space + 1
print(count_h, count_e, count_l,
      count_o, count_space)

# well that was terrible let's do it with a dict

# before we can start looping and
# doing stuff, we need to know a bit
# more dict syntax

# create an empty dict
example = {} # dict()
# add something into it
example['key'] = 'value'
print(example)
# update an existing value
example['key'] = 'something else'
print(example)
# get stuff out of a dictionary
print(example['key']) # we get the literal value back

# how we can populate a dict
# text = "hello fellow humans"
# letters1 = {}
# for char in text:
#     letters1[char] = 'found one'
# print(letters1)\

text = "hello fellow humans"
letters1 = {} # the "logic" method
for char in text:
    if char in letters1: # if the key is already in there
        letters1[char] = letters1[char] + 1 # increment
    else: # if not in there yet
        letters1[char] = 1 # establish the base
print(letters1)

# prepopulation pattern
letters2 = {}
# first just add all the key/value pairs
for char in text:
    letters2[char] = 0 # establish
for char in text:
    # letters2[char] = letters2[char] + 1
    letters2[char] += 1 # same

# prepopulation variation: pop/sample
import string
letters3 = {}
for char in string.ascii_lowercase + string.punctuation + " ":
    letters3[char] = 0 # establish
for char in text:
    letters3[char] += 1 # increment
print(letters3)

print(letters3)

# all the shortcuts in one, the "get" pattern

letters4 = {}
for char in text:
    letters4[char] = letters4.get(char, 0) + 1
print(letters4)