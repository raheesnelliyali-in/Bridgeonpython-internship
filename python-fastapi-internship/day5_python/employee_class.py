class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
    def get_info(self):
        return f"Name: {self.name}, Department: {self.department}, Salary: ₹{self.salary}"
    def __str__(self):
        return f"{self.name} works in {self.department} and earns ₹{self.salary}"
emp1 = Employee("Rahees", "IT", 80000)
emp2 = Employee("Sahad", "HR", 25000)
print(emp1.get_info())
print(emp1)
print(emp2.get_info())
print(emp2)