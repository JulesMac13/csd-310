from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.efksc.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

collection = db.students

peter = {"Student_ID": "1007", "First_Name": "Peter", "Last_Name": "Quill"}

rocket = {"Student_ID": "1008", "First_Name": "Rocket", "Last_Name": "Racoon"}

drax = {"Student_ID": "1009", "First_Name": "Drax", "Last_Name": "the Destroyer"}

peter_student_id = collection.insert_one(peter).inserted_id

rocket_student_id = collection.insert_one(rocket).inserted_id

drax_student_id = collection.insert_one(drax).inserted_id

print("-- INSERT STATEMENTS --")

print("Inserted student record Peter Quill into the students collection with document_id " + str(peter_student_id))

print("Inserted student record Rocket Racoon into the students collection with document_id " + str(rocket_student_id))

print("Inserted student record Drax the Destroyer into the students collection with document_id " + str(drax_student_id))