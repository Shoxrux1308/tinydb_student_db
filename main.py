from tinydb import TinyDB, Query

# Create or connect to the database
db = TinyDB('students.json',indent=4)

new_students=[
    {
    "id": 4,
    "name": "Azizbek",
    "age": 20,
    "gender": "Male",
    "contact": "941232277",
    "grade_level": "2004",
    "subjects": {
        "math": 95,
        "science": 95,
        "english": 90
    },
    "attendance": 98,
    "activities": ["Basketball", "English Course"],
    "address": {
        "street": "Baghdad St",
        "city": "Samarkand",
        "state": "Uzbekistan",
        "zip_code": "1040100"
    }
    },
    {
        "id": 5,
        "name": "Asilbek",
        "age": 19,
        "gender": "Male",
        "contact": "940401520",
        "grade_level": "2005",
        "subjects": {
            "math": 90,
            "science": 85,
            "english": 90
        },
        "attendance": 95,
        "activities": ["Basketball", "English Course","Football"],
        "address": {
            "street": "Baghdad St",
            "city": "Samarkand",
            "state": "Uzbekistan",
            "zip_code": "1040100"
        }
    },
    {
        "id": 6,
        "name": "Shahzobbek",
        "age": 21,
        "gender": "Male",
        "contact": "940016556",
        "grade_level": "2003",
        "subjects": {
            "math": 85,
            "science": 90,
            "english": 95
        },
        "attendance": 90,
        "activities": ["Basketball", "English Course","Volleyball"],
        "address": {
            "street": "Amir Temur St",
            "city": "Samarkand",
            "state": "Uzbekistan",
            "zip_code": "1040100"
        }
    }
    ]
db.insert_multiple(new_students)
# Reference the default table
# students_table = db.table("_default")
# print(students_table.all())
