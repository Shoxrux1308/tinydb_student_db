from tinydb import TinyDB, Query

# Create or connect to the database
db = TinyDB('students.json',indent=4)

students=[
    {
    "id": 1,
    "name": "Shoxrux",
    "age": 19,
    "gender": "Male",
    "contact": "940500320",
    "grade_level": "2005",
    "subjects": {
        "math": 85,
        "physics": 90,
        "english": 88
    },
    "attendance": 90,
    "activities": ["english course","programming course","Football", "Volleyball"],
    "address": {
        "street": "Bag'dod St",
        "city": "Samarkand",
        "state": "Uzbekistan",
        "zip_code": "140100"
    }

},
    {
    "id": 2,
    "name": "Abdumajid",
    "age": 18,
    "gender": "Male",
    "contact": "941252409",
    "grade_level": "2005",
    "subjects": {
        "math": 90,
        "biology": 90,
        "english": 88
    },
    "attendance": 95,
    "activities": ["english course","programming course","Football"],
    "address": {
        "street": "Amir Temur St",
        "city": "Samarkand",
        "state": "Uzbekistan",
        "zip_code": "140100"
    }

    },
    {
    "id": 3,
    "name": "Mehrojiddin",
    "age": 19,
    "gender": "Male",
    "contact": "947077005",
    "grade_level": "2005",
    "subjects": {
        "math": 85,
        "history": 90,
        "english": 95
    },
    "attendance": 85,
    "activities": ["english course","programming course","Football", "Volleyball"],
    "address": {
        "street": "Motrid St",
        "city": "Samarkand",
        "state": "Uzbekistan",
        "zip_code": "140100"
    }

}
]
db.insert_multiple(students)
# Reference the default table
# students_table = db.table("_default")
# print(students_table.all())
