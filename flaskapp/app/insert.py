import pymysql
import csv

db = pymysql.connect(
    host="localhost",
    port=3306,
    db="flasksteam",
    user="root", 
    password="1qazxc"
)

cursor = db.cursor()

tags = []
tagid = []

with open('unique_tags.csv', 'r') as raw:
    lines = raw.readlines()
cooked = csv.reader(lines)
for record in cooked:
    tags.append(record[1])
    tagid.append(record[0])

# print(tags)

print(len(tagid), len(tags))
tagid.pop(0)
tags.pop(0)
print(len(tagid), len(tags))

print('0---------------0')


SQL = '''
        INSERT INTO `taglist` 
        VALUE("{tagid}", "{tags}")
    '''
for i in range(len(tagid)):
    print(tagid[i], tags[i])
    cursor.execute(SQL.format(tagid=int(tagid[i]), tags=str(tags[i])))

db.commit()