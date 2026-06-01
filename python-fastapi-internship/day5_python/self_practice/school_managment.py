class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def grade(self, mark):
        if mark >= 90:
            return "A"
        elif mark >= 75:
            return "B"
        elif mark >= 50:
            return "C"
        else:
            return "F"


class Teacher(Person):
    def assign_grade(self, student, mark):
        print(f"{student.name} got Grade {student.grade(mark)}")


student1 = Student("Rahees", 22)
teacher1 = Teacher("Arun", 35)

teacher1.assign_grade(student1, 85)