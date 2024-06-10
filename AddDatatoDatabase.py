import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-46d78-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1":
        {
            "name": "Anshul Verma",
            "major": "Web Dev",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2024-04-14 00:54:34"
        },
    "2":
        {
            "name": "Champa",
            "major": "Java",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2024-04-14 00:54:34"
        },
    "3":
        {
            "name": "Chandra Kant Budhalakoti",
            "major": "MERN",
            "starting_year": 2022,
            "total_attendance": 10,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2024-04-14 00:54:34"
        },
    "4":
        {
            "name": "Dikshant Kandpal",
            "major": "JAVA",
            "starting_year": 2022,
            "total_attendance": 6,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2024-04-14 00:54:34"
        },
    "5":
        {
            "name": "Jagdish Singh Bisht",
            "major": "JavaScript",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2024-04-14 00:54:34"
        },
    "6":
        {
            "name": "Jyoti Joshi",
            "major": "FrontEnd",
            "starting_year": 2022,
            "total_attendance": 4,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2024-04-14 00:54:34"
        },
    "7":
        {
            "name": "Nisha Joshi",
            "major": "FrontEnd",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2024-04-14 00:54:34"
        },
    "8":
        {
            "name": "Deepak Papney",
            "major": "MySQL",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "Bad",
            "year": 4,
            "last_attendance_time": "2024-04-14 00:54:34"
        },
    "9":
        {
            "name": "Sanjay Dutt",
            "major": "Dot net",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2024-04-14 00:54:34"
        },
    "10":
        {
            "name": "Neeraj Kumar",
            "major": "Python",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2024-04-14 00:54:34"
        },
    "11":
        {
            "name": "Rohit Chandra",
            "major": "Java",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2024-04-14 00:54:34"
        },
    "12":
        {
            "name": "Vikram Kumar",
            "major": "FrontEnd",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2024-04-14 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)