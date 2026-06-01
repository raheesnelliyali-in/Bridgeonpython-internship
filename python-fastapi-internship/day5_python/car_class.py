class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    def drive(self, km):
        self.odometer += km
        print(f"Driven {km} km")
    def get_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Odometer: {self.odometer} km")
car1 = Car("Toyota", "Etios Liva", 2019)
car1.drive(0)
car1.drive(32000)
car1.get_info()