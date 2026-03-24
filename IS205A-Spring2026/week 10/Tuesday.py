# for letter in "abc":
#     print(letter)
#
words = ['dog', 'cat', 'boat', 'horse']
lines = ['line 1 here', 'line 2 here',
         'line 3 here', 'line 4 here']

for w in words:
    print(w)
for l in lines:
    print(l)

# that's not what we're after
# we want all the pairs

# nested here is what gets us the pairs
for w in words:
    for l in lines:
        print(w, l)

for l in lines:
    for w in words:
        print(w, l)

### let's read in this file

infile = open('animalsarecool.txt', 'rt', encoding='utf-8')
lines = infile.readlines()
infile.close()

# print(lines)
# for w in words:
#     for l in lines:
#         # print(w, w in l, l.strip())
#         if w in l:
#             print(w, l.strip())

# so we can see the positive matches for each
# let's set this to the side
# and look at how to programmatically make files

# for w in words:
#     # print(w + "-results.txt") # this is our file name
#     fname = w + "-results.txt"
#     # now we can make the file
#     outfile = open(fname, 'wt',encoding='utf-8')
#     outfile.write("hello there, there will be text later")
#     outfile.close()

# where you are writing stuff to the file is where
# your inner loop should go
for w in words:
    # print(w + "-results.txt") # this is our file name
    fname = w + "-results.txt"
    # now we can make the file
    outfile = open(fname, 'wt',encoding='utf-8')
    for l in lines: # now loop over lines
        if w in l: # no fancy checks
            outfile.write(l) # write line to file
    outfile.close() # indent should remain same as creation