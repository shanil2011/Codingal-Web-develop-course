def substrct(x,y):
    return x-y
def addition(x,y):
    return x+y
def multiply(x,y):
    return x * y
def division(x,y):
    return x / y

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum :" , addition(num1,num2))
print("Substraction :" , substrct(num1,num2))
print("Multiplication :" , multiply(num1,num2))
print("Division :" , division(num1,num2))

