class InvalidMarkError(Exception):
    pass


def calculate_grade(name: str, *marks: int) -> str:
    if not marks:
        raise InvalidMarkError("No marks provided")

    for mark in marks:
        if mark < 0 or mark > 100:
            raise InvalidMarkError("Mark must be between 0 and 100")

    average: float = sum(marks) / len(marks)

    if average >= 90:
        grade: str = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    return f"{name} - Average: {average:.2f}, Grade: {grade}"


def generate_report(students: list[tuple[str, list[int]]]) -> None:
    print("Student Grade Report")
    print("-" * 30)

    for name, marks in students:
        try:
            result: str = calculate_grade(name, *marks)
            print(result)
        except InvalidMarkError as error:
            print(f"{name} - Error: {error}")


students: list[tuple[str, list[int]]] = [
    ("Rahees", [90, 85, 95]),
    ("Akhil", [70, 80, 75]),
    ("Ravi", [150, 80, 90]),
    ("Anu", []),
]

generate_report(students)