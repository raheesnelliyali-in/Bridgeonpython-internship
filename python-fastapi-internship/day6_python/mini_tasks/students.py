import json
students = [
    {"name": "Rahees", "mark": 90},
    {"name": "Sahad", "mark": 85},
    {"name": "Refai", "mark": 78},
    {"name": "Saad", "mark": 92},
    {"name": "Arun", "mark": 89}
]
with open("students.json", "w") as file:
    json.dump(students, file, indent=2)
    