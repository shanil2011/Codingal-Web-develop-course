class student:
    grade = 10
    name = "UwU Penguin"
    def introduction(self):
        print("Hello,I am a student")
    def details(self):
        print("My name is",self.name)
        print("I am in grade",self.grade)

ob = student()
ob.introduction()
ob.details()
