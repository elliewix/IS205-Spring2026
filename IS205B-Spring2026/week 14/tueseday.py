infile = open('text.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()

start = text.find("start") + len("start")
end = text.find("end")
# print(text[start:end])
middle = text[start:end]
print(middle.split("\n"))
print(middle.splitlines())

# don't do this
# don't make me cry
lines = text.splitlines()

print(lines)
count = 0
for l in lines:
    if "start" in l:
        start = count
    if "end" in l:
        end = count
    count += 1
print(start, end)

# you can also do this with lines

infile = open('text.txt', 'rt', encoding='utf-8')
lines = infile.readlines()
infile.close()
print(lines)

start = lines.index("start\n") +1
end = lines.index("end\n")
print(lines[start:end])

# you can actually correct for newlines
infile = open('text.txt', 'rt', encoding='utf-8')
lines = infile.read().splitlines(keepends=False)
infile.close()
print(lines)

