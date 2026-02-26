# range function
print(range(10))
# to see the numbers, recast to a list
print(list(range(10))) # stop
print(list(range(2,9))) # start, stop,2-8 inc
print(list(range(2, 9, 2))) # start stop step

# indexing and slicing
## indexing is to get "one" thing out
## by position
print("hello"[0]) # gives h, "first"
print("hello"[-1]) # gives o, "last"
print("hello"[2])

# when I slice on a string

print("hello"[1:5])
print("hello"[1:4])
print("hello"[-4:-1])
print("hello"[:3]) # omit start, uses 0)
print("hello"[2:]) # omit stop, go to end
print("hello"[:]) # give everything
print("hello"[::-1])
print("hello"[::2])
# when I index on a string.....
# I get a single character back

# if I index on a list......

letters = ['a', 'b', 'c']
nums = [7, 8, 9]
# when you index a list....
# you get that actual object back
print(letters[1]) # b as a string
print(nums[1]) # 8 as an int

# but now, slicing....
# you ALWAYS get a list back
# with that content, no matter how
# many results there are

letters = ['a', 'b', 'c']
nums = [7, 8, 9]

print(letters[1:])
print(nums[1:])
print(letters[2:])
print(letters[3:])

# now for files
# our core infile pattern is....
infile = open('mytext.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()
print(text)

## another pattern
infile = open('mytext.txt', 'rt', encoding='utf-8')
for line in infile:
    print(line)
infile.close()