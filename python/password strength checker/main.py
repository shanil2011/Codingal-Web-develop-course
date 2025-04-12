
from tkinter import *

enter = input("Enter something: ")
running = True
print("Before we start this program , this might take longer than expected , please be patient.You have to click enter multiple time.")

num1 = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
num2 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
num3 = "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "?", "/", "|", "{", "}", "[", "]", ";", ":", "'", '"', "<", ">", ",", ".", "/", "?"

while running:

    if len(input()) > 20:
        print("Your password  is too long!")
    
    if len(input()) < 3:
        print("Your password is too short!")

    if len(input()) == 0:
        print("You didn't enter anything!")

    if input() not in [num1]:
        print("Your password is weak!")

    if input() not in [num3]:
        print("Your password is weak!")

    if input() not in [num2]:
        print("Your password is weak!")

    if any(char in num1 for char in enter) and any(char in num2 for char in enter) and any(char in num3 for char in enter):
        print("Your password is strong!")

if input() == "exit":
    print("Exiting...")
    running = False
