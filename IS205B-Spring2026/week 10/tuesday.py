# all about nested loops

words = ['cat', 'dog', 'boat', 'horse']
lines = ['line 1', 'line 2', 'line 3', 'line 4']

# sometimes people try a linear way
# which isn't what we want

for w in words:
    print(w)
for l in lines:
    print(l)

# we need to loop over them together
# which goes outer and which is inner?

for w in words:
    for l in lines:
        print(w, l)

for l in lines:
    for w in words:
        print(w, l)

# now that I can make a cross product
# I can use the content together

# let's read in our actual data

infile = open('animalsarecool.txt','rt', encoding='utf-8')
lines = infile.readlines()
infile.close()
print(lines)

# for l in lines:
#     print(l.strip())

for w in words:
    for l in lines:
        # print(w, w in l, l.strip())
        if w in l:
            print(w,l.strip())

# let's set that aside for now and explore
# how to programmatically create files

print(words)
for w in words:     # remember that file names are just strings
    # print(w + "-results.txt")
    fname = w + "-results.txt"
    outfile = open(fname, 'wt', encoding='utf-8')
    outfile.write("the actual text will be here soon")
    outfile.close()

### let's put them together

for w in words:
    outfile = open(w + "-results.txt", 'wt', encoding='utf-8')
    # print(outfile)
    for l in lines:
        if w in l:
            outfile.write(l)
    outfile.close()