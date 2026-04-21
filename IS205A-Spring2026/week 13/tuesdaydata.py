import json

infile = open('results.json', 'rt', encoding='utf-8')
data = json.load(infile)
infile.close()

print(data)

# ceey's fav classes
print(data["Ceey"]['fav_classes'])
# Beee's credit hours
print(data["Beee"]['credits'])