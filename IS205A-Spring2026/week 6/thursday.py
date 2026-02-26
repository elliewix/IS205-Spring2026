# range function
print(range(10)) # this would be fine in a for loop
# but we can't the numbers
# to see them, recast as a list
print(list(range(10))) # 0-9 inc
print(list(range(2, 8))) # start, stop
print(list(range(0,10,2))) # start, stop, step

# indexing/slicing

## indexing is used to get a single thing
## out of a structure

### indexing: no colon
#strings
print("hello"[0]) # give you h
## "the first" [0]
## "the last" [-1]

### slicing: there's a colon
print("hello"[1:4]) #ell
print("hello"[-4:-1])

# when you omit start, it presumes the beginning
# when you omit stop, it presumes the end
print("hello"[2:]) # 2th to the end
print("hello"[:]) # the whole thing
print("hello"[::-1]) # whole thing reversed
print("hello"[::-2])

# now for lists which are different

letters = ['a', 'b', 'c']
nums = [6, 7, 8]
print(letters[1]) # b the string
print(nums[1]) # 7 the int

# but if I slice
print(letters[1:])
print(nums[1:])
print(letters[2:])
print(letters[3:])

## okay working with files

# infile pattern
# step 1, make infile
infile = open('mytext.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()
print(text)

# another way
infile = open('mytext.txt', 'rt', encoding='utf-8')
for line in infile:
    print(line)

infile.close()

