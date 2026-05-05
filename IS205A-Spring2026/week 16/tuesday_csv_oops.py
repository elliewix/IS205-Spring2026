words = ['animals, n\'ame\'s', 's"words"', 'table', 'yeet']

# let's make a csv with the columns:
# word, length, first letter, last letter, reversed
headers = ['word', 'length', 'first letter',
           'last letter', 'reversed']
all_rows = []
for w in words:
    # print([w, len(w), w[0], w[-1],w[::-1]])
    row = [w, len(w), w[0], w[-1],w[::-1]]
    all_rows.append(row)

print(all_rows)
import csv
csvout = csv.writer(open('data.csv', 'wt',
                         encoding='utf-8', newline = ""))
csvout.writerow(headers) # the singular one
csvout.writerows(all_rows) # your 2d data