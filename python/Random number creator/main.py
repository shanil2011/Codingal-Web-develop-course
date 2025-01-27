import random

low = 1
high = 100

number = random.randint(low, high)

print("There are 100 integer in here.") # This is a comment
num1 = int(input("Enter the number: "))

if num1>= number:
    print("Your number is low.Try again by clicking the run option and the number was" , number)
elif num1<= number:
    print("Your number is high.Try again by clicking the run option" , number)
else:
    print("Your number is correct.")

