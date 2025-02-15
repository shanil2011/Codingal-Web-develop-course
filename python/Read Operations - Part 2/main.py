file = open("Codingal.txt", "r")
print("Reading first line ........")
print(file.readline())
file.close()

file = open("Codingal.txt", "r")
print("Reading Multiple lines ........")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open("Codingal.txt", "r")
print("looping through the lines ........")
for line in file:
    print(line)
file.close()