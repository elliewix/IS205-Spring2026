animals = ("Rat, Ox, Tiger, Rabbit, Dragon, Snake, "
           "Horse, Goat (or Sheep/Ram), Monkey, "
           "Rooster, Dog, Pig")

# let's remove the extra bit
animals = animals.replace(" (or Sheep/Ram)", "")
# now lowercase the text
animals = animals.lower()
# except do it all in one line
# print(animals.split(", "))
animal_names = animals.split(", ")
print(animal_names)

for name in animal_names:
    name = name.upper()
    print(name.replace('A', 'x') + " is a zodiac animal")

# let's look at a for loop where we are
# iteratively updating content

# we want to go through all these names
# and change the vowels to x
# because we're cool and that's cool

vowels = "aeiou".upper()
one_animal = "rooster".upper()
for v in vowels:
    one_animal = one_animal.replace(v, 'x')
    print(one_animal)
