class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def infoself(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Meow")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def infoself(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Woof")
cat1 = Cat("Mike", 2.5)
dog1 = Dog("Tyson", 8)

for animat in (cat1, dog1):
    animat.infoself()
    animat.make_sound()
