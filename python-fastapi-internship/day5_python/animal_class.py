class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def speak(self):
        print(self.sound)
        
class Dog(Animal):
    def speak(self):
        print("woof woof")
class cat(Animal):
    def speak(self):
        print("meow meow")
dog=Dog("Tommy","woof")
cat=cat("Kitty","meow")
print(dog.name)
dog.speak()

print(cat.name)
cat.speak()