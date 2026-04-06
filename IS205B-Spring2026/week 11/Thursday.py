text = "I'm very tired, and maybe you are, too. Thursdays are always hard but I'm glad to see B section because I can now shut up for the week."
data = {}
# prepop pattern
for t in text:
    data[t] = 0
for t in text:
    data[t] += 1
print(data)

from collections import Counter
# don't use this on the homework
# print(Counter(text))

# dict extraction and looping
print(data[' '] + data[","] + data["'"] + data["."])

# dict extraction methods
print(data.keys())
print(data.values())
print(sum(data.values())/len(data.keys()))

# looping
print(data.items())
# gets the job done
for key in data.keys():
    print(key, data[key])

# slightly "better" way
# for key, value in data.items():
#     print(key, value)

for char, count in data.items():
    # print(char, count
    print(char * count)