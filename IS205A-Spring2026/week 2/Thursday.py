print("hello for lab 1")

# data type review

## numerical
print(6) # integer
print(7.0) # float
print(8.45) # also float
## string
print('10')
print("11")
print("""12""")

## Boolean
print(True) # case matters
print(False)

## None
print(None) # no null, we have None

# variables

## some keywords you just can't
## also can't start with numbers

## the content owns the name
## the name doesn't own the content

name = "Elizabeth"
print(name)
name2 = "Phillip"
print(name2)
## concat strings
print(name + name2)

# set integers
x_coord = 3
y_coord = 4
print(x_coord, y_coord)
# do math
print(x_coord * 1.4, y_coord * 2.3)

# pretend we're messing with a game
z_point = 7 #original value
move = 4 # move these many "spaces"
## update the z_point with the "move"
z_point = z_point + move # updating a variable
print(z_point)