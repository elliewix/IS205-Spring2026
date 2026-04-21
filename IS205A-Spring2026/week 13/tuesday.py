studentinfo = {}

students = ['Aaaay', 'Beee', "Ceey"]
# goal: capture some info about them
# credit hours, fav classes

{"Aaaay": {"credits": 15, "fav_classes": ['IS202', 'IS206']},
 "Beee": {"credits": 12, "fav_classes": ['IS101', 'IS204']}}

# prepopulation pass
for person in students:
    studentinfo[person] = {"credits": 0, "fav_classes": []}

print(studentinfo)

stu = "Beee"
credits = [3, 3, 4, 2]
for c in credits:
    studentinfo[stu]["credits"] += c
print(studentinfo)

studentinfo["Aaaay"]["fav_classes"].append('IS202')
print(studentinfo)
studentinfo["Ceey"]["fav_classes"].append("IS308")
studentinfo["Ceey"]["fav_classes"].append("IS145")
studentinfo["Ceey"]["fav_classes"].append(['fav2', 'fav3']) # not great
studentinfo["Ceey"]["fav_classes"].extend(['fav5', 'fav6', 'fav7']) # extend if you have a list of stuff
print(studentinfo)


import json # should be a the very top
outfile = open('results.json', 'wt', encoding='utf-8')
json.dump(studentinfo, outfile, indent = 4)
outfile.close()

