import json

infile = open('results.json', 'rt', encoding='utf-8')
data = json.load(infile)
infile.close()

print(data)

# Beee's credit hours
print(data["Beee"]['credits'])

# Ceey's fav classes
print(data["Ceey"]["fav_classes"])