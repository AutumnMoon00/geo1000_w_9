import dbm

db = dbm.open('captions', 'c')

db["cleese.png"] = "photo of John Cleese."

key_name = db["cleese.png"]
print(key_name)

db["cleese.png"] = "photo of John Cleese doing a silly walk."
print(db["cleese.png"])

for key in db.keys():
    print(key, db[key])

db.close()