
db = {}

for i in range(4):
    name = raw_input('name: ')
    name_id = int(raw_input('name_id: '))
    db[name_id] = name
print db

for id in sorted(db):
    print id, db[id]

