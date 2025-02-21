firstfile = input("Enter the first file name: ")
secondfile = input("Enter the second file name: ")

f1 = open(firstfile, "r")
f2 = open(secondfile, "r")

print("Content before first file appending -\n" , f1.read())
print("Content before second file appending -\n" , f2.read())

f1.close()
f2.close()

f1 = open(firstfile, "a+")
f2 = open(secondfile, "r")

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print("Content after first file appending -\n" , f1.read())
print("Content after second file appending -\n" , f2.read())

f1.close()
f2.close()
