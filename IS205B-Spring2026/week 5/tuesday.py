animals = ("Rat Ox Tiger Rabbit Dragon Snake "
           "Horse Goat (or Sheep/Ram) Monkey "
           "Rooster Dog Pig")
animals = animals.replace(" (or Sheep/Ram)", "")
animals = animals.lower()

# print(animals.split())
animal_names = animals.split()
print(animal_names)
# let's loop over our content
for name in animal_names:
    name = name.upper()
    print(len(name), name.replace("A", "x") + " is a zodiac animal")

# say we want to change all the vowels to x
vowels = "aeiou".upper()
s = "rooster".upper()
for v in vowels:
    # print(s.replace(v, 'x'))
    s = s.replace(v, 'x')
    print(s)