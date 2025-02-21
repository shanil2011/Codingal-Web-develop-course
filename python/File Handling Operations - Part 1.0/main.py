with open("Codingal.txt", "w") as file:
    file.write("Hello, Codinga!")
file.close()

with open("Codingal.txt", "r") as file:
    data = file.readlines()
    print("Words in the file are:")
    for line in data:
        word = line.split()
        print(word)
file.close()