outputFile = open("Updatedfiles.txt", "w")

inputfile = open("Repeatedfiles.txt", "r")

lines_seen_so_far = set()

print("Elimilating Duplicate lines........")

for line in inputfile:

    outputFile.write(line)

    lines_seen_so_far.add(line)

inputfile.close()
outputFile.close()