class Employee:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        print("Employee created")
    def __del__(self):
        print("Destructor created , Employee destroyed")

num1 = 10
num2 = 20
num3 = 30
obj = Employee(num1, num2, num3)
del obj


