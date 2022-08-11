from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.efksc.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

collection = db.students

from pprint import pprint

records = collection.find({}, {"Student_ID":1, "First_Name":1, "Last_Name":1, "_id":0})

print("DISPLAYING STUDENT DOCUMENTS FROM find() QUERY")

for record in records:

    pprint(record)
 
record = collection.find_one({"Student_ID":"1007"}, {"Student_ID":1, "First_Name":1, "Last_Name":1, "_id":0})
 
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")

pprint(record)

#Cannot for the life of me after a couple of hours of searching Google on how to get the documents to print cleaner and on separate lines simultaneously