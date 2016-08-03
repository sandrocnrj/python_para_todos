import pymongo
import csv
import os

conn = pymongo.MongoClient()

db = conn.pythondb

cursor = db.pessoas.find({},{'_id':1, 'nome': 1})

with open('pessoas.csv', 'w') as outfile:
    fields = ['_id','nome']
    writer = csv.DictWriter(outfile, fieldnames=fields)
    writer.writeheader()
    for x in cursor:
        writer.writerow(x)

outfile.close()
