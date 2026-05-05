words = ['apples, many', 'ca,nvas', 'tues"d,ay"', 'door']

# our csv for this should have:
# word, length, first letter, last letter, reverse
all_rows = []
for w in words:
    # print([w, len(w), w[0], w[-1], w[::-1]])
    row = [w, len(w), w[0], w[-1], w[::-1]]
    all_rows.append(row)
print(all_rows)

headers = ['word', 'length', '1st, letter',
           '2nd, letter', 'reverse']

# only when you have all the rows and the headers
# should you attempt the csv

import csv

csvout = csv.writer(open('data.csv', 'wt', newline=''))
csvout.writerow(headers) # singular
csvout.writerows(all_rows) # plural