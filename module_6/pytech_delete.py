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

#insert method

groot = {"Student_ID": "1010", "First_Name": "Groot", "Last_Name": "None"}

groot_student_id = collection.insert_one(groot).inserted_id

print("-- INSERT STATEMENTS --")

print("Inserted student record Groot into the students collection with document_id " + str(groot_student_id))

records = collection.find({"Student_ID":"1010"})

print("DISPLAYING STUDENT TEST DOCUMENT")

for record in records:

    pprint(record)

#drop method



# print("DISPLAYING STUDENT DOCUMENTS FROM find() QUERY")

# for record in records:

#     pprint(record)