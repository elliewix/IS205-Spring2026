infile = open('Three-years-in-europe.txt', 'rt', encoding='utf-8')
# text = infile.read()
text_lines = infile.readlines()
infile.close()

# print(text_lines)
# for line in text_lines:
#     # print(len(line) >= 70)
#     if len(line) >= 70:
#         print(line)
print(len(text_lines))
# how about counting the number of results
count = 0 # outside of and before my for loop
for line in text_lines:
    # print(len(line) >= 70)
    if len(line) >= 70:
        count = count + 1 # increment the count
        # count += 1
print(count)

###

# outfile pattern
outfile = open('myresults.txt', 'wt', encoding='utf-8')
outfile.write("hello from tuesday.py")
outfile.close()

## how does this connect in a loop

# we'll start from the top
## load the file
infile = open('Three-years-in-europe.txt', 'rt', encoding='utf-8')
text_lines = infile.readlines()
infile.close()

## loop over the contents
# for line in text_lines:
#     if len(line) >= 70:
#         print(line)
# add the outfile
outfile = open('moreresults.txt','wt',encoding='utf-8')
for line in text_lines:
    if len(line) >= 70:
        # print(line)
        outfile.write(line)
outfile.close() # close after the loop to work inside