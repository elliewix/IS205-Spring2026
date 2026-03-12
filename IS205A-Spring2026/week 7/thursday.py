from transformers.models.megatron_bert.convert_megatron_bert_checkpoint import recursive_print

text = "--Foo-Bar's.\""
print(text)

print(text.replace('"', ''))
# individually but inside the whole thing

# let's try out strip
text = "--Foo-Bar's.\""
print(text.strip("-\".")) # don't type them all in
import string
print(text.strip(string.punctuation))
# to apply this across a line of text and words
# we need to split the words
text = "today I've visit'd \"--Foo-Bar's.\""
print(text)
print(text.split())
# we can loop over it
for w in text.split(): # w for word
    print(w.strip(string.punctuation)) # do what we did before
    # just inside the loop

# to reconnect everything we want to use a list
# accumulator pattern
# our core looping pattern
# for num in range(5, 10): # looping over some content
#     newnum = num * 1.2
#     print(newnum)

# add a list accumulator into this
recalculated = []
for num in range(5, 10): # looping over some content
    newnum = num * 1.2
    print(newnum) # this variable has what we want
    recalculated.append(newnum) # collect it with append
    # NO ASSIGNMENT STATEMENT WITH APPEND

print(recalculated)

# example of why we don't want an assignment statement
list_x = ['a', 'b']
list_x.append('c') # this is how you do it
print(list_x)
list_x = list_x.append('d') # not how you do it
print(list_x)

## we've got this list now.....

print(recalculated)

# okay so let's go back to where we started

text = "today I've visit'd \"--Foo-Bar's.\""
cleaned = []
for w in text.split(): # split it
    clean = w.strip(string.punctuation) # clean it
    cleaned.append(clean) # collect it
print(cleaned)

# you can use .join to put this back into a string
print("x".join(['C', 'A', 'T']))
print(text)
print(text.split())
print(cleaned)
print(" ".join(cleaned))