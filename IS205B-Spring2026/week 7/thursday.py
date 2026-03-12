text = "(mother-in-law) --\"foo-bar's\"--"

print(text)
print("hw2 would have been motherinlaw foobars")

# hw3 has us taking a diff approach
## we'll be using the strip method
# normally we see strip in the context
# of removing space characters
# but you can give it specific things to
# look for instead, each treated separately

text = "(mother-in-law) --\"foo-bar's\"--"
# print(text.strip('.,"()-')) # don't type them all out
# use string!
import string
print(text.strip(string.punctuation))
# this fixes one thing, getting stuff off ends
text = "(mother-in-law) --\"foo-bar's\"-- cat's."
print(text)
print(text.split()) # break it apart
for w in text.split(): # loop over the broken up text
    print(w.strip(string.punctuation)) # clean it up

# good: cleaned up! bad: still separate
# new pattern: collecting things is a
# list accumulator pattern

for num in range(5, 10):
    print(num * 1.2)
# let's add a list accumulator pattern
recalulated = []
for num in range(5, 10):
    print(num * 1.2)
    # no assignment statement
    recalulated.append(num * 1.2)
print(recalulated)

# let's talk about why not assignment
list_x = []
list_x.append('a') # DO IT THIS WAY
# print(list_x)
list_x = list_x.append('b') # NOT THIS WAY
# print(list_x) # see None

##
text = "(mother-in-law) --\"foo-bar's\"-- cat's."
cleaned = []
for w in text.split(): # split it and loop
    clean = w.strip(string.punctuation) # clean it
    cleaned.append(clean) # collect it
print(cleaned)

# let's look at join

print("X".join(['c', 'a', 't']))
print(" ".join(cleaned))

### see all the results together
print(text)
print(text.split())
print(cleaned)
print(" ".join(cleaned))