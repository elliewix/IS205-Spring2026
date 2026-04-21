studentinfo = {}

names = ['Aaay', 'Beee', "Ceey"]

for name in names:
    studentinfo[name] = {"credits": 0, "fav_classes": []}

# .... "Aaay": {"credits": num, "fav_classes": [stuff] }
print(studentinfo)

# mess with credit hours first
hours = [3, 3, 4, 2, 3] # Beee's credits

for c in hours:
    studentinfo["Beee"]["credits"] += c

print(studentinfo)

print(studentinfo["Aaay"])
print(studentinfo["Aaay"]["fav_classes"])

studentinfo["Aaay"]["fav_classes"].append("IS202")
studentinfo["Aaay"]["fav_classes"].append('IS380')
print(studentinfo)
studentinfo["Beee"]["fav_classes"].append("390DG")
studentinfo["Aaay"]["fav_classes"].append("205")
studentinfo["Ceey"]["fav_classes"].append("143")
print(studentinfo)
studentinfo["Aaay"]["fav_classes"].append(['204', '206'])
print(studentinfo)
studentinfo["Ceey"]["fav_classes"].extend(['204', '206'])
print(studentinfo)

# once the data is ready, you write it out as a json
import json # remember this should at the very top

outfile = open('results.json', 'wt', encoding='utf-8')
json.dump(studentinfo, outfile, indent = 4)
outfile.close()

