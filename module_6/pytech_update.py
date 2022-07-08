from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.efksc.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

collection = db.students

from pprint import pprint

records = collection.find({})

print("DISPLAYING STUDENT DOCUMENTS FROM find() QUERY")

for record in records:

    pprint(record)

#update method 
#MongoDB: update_one Example
#result = db.collection.update_one({“student_id”: 1007}, {“$set”: {“last_name”: “Smith”}})

peter_student_id = db.collection.update_one({"Student_Id": 1007}, {"$set": {"Last_Name": "Star-Lord"}})
 
record = collection.find_one({"Student_ID":"1007"})
 
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")

pprint(record)