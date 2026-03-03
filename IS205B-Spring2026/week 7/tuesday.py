infile = open('Three-years-in-europe.txt',
              'rt', encoding='utf-8')
# text = infile.read()
text_lines = infile.readlines()
infile.close()
# print(text_lines)

# let's loop over the lines
# for line in text_lines:
#     print(line.strip())
#
# print(len(text_lines))

# put in a filter now
# for line in text_lines:
#     # print(len(line) >= 70)
#     if len(line) >= 70:
#         print(line)

# add in a counter
# outside of and before my loop
count = 0 # set the base
for line in text_lines:
    # print(len(line) >= 70)
    if len(line) >= 70:
        # print(line)
        count = count + 1
print(count) # outside of and after

# outfile pattern
## core pattern
outfile = open('myresults.txt', 'wt', encoding='utf-8')
outfile.write('Hello from tuesday.py')
outfile.close()

# let's restart from the top

## read in the file
infile = open('Three-years-in-europe.txt', 'rt', encoding='utf-8')
text_lines = infile.readlines()
infile.close()

# # loop over the content
# for line in text_lines:
#     if len(line) >= 70:
#         print(line) # now print only some
# now we add the outfile pattern
outfile = open('longlines.txt', 'wt', encoding='utf-8')
for line in text_lines:
    if len(line) >= 70:
        # print(line) # now print only some
        outfile.write(line)
outfile.close()

# don't do this

# with open('longlines.txt', 'wt', encoding='utf-8') as outfile:
#     for line in text_lines:
#         if len(line) >= 70:
#             # print(line) # now print only some
#             outfile.write(line)