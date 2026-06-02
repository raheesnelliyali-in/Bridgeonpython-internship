import json

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    print(
        f"Name: {student['name']}, "
        f"Mark: {student['mark']}"
    )