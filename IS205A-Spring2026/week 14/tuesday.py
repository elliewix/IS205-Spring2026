infile = open('text.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()

s = text.find("start")
e = text.find("end")
print(text[s + len("start"):e])
data = text[s + len("start"):e]
print(data.split("\n"))
print(data.splitlines())

## starting with a list

infile = open('text.txt', 'rt', encoding='utf-8')
lines = infile.readlines()
# lines = infile.read().splitlines(keepends=False) # this cleans it up
infile.close()

s = lines.index("start\n")
e = lines.index("end\n")
print(lines[s + 1:e])

# don't do this, overkill

count = 0
for l in lines:
    if "start" in l:
        s = count
    if "end" in l:
        e = count
    count += 1
print(lines[s + 1: e])\