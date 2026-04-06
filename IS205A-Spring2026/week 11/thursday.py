data = {}
text = "I'm very tired, maybe you are too. Play nicely this weekend."

for t in text:
    data[t] = 0

for t in text:
    data[t] += 1

print(data)

# dict extraction and looping
print(data[' '])
print(data[' '] + data["'"] + data['.'])

# looping over dicts

# works just fine
for k in data.keys():
    print(k, data[k])

# the "better" way but arguments can be made

# for key, value in data.items():
#     print(key, value)

for char, count in data.items():
    print(char * count)

infile = open('animalsarecool.txt', 'rt')
text = infile.read()
infile.close()

chars = {}
text = text.replace(" ", '_')
text = text.replace('\n', 'X')
for t in text:
    if t in chars:
        chars[t] += 1
    else:
        chars[t] = 1

print(chars)

for char, count in chars.items():
    print(char * count)

print(sum(chars.values())/len(chars.keys()), "avg time each letter appears")

print(chars.keys())
print(chars.items())