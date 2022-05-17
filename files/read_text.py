# Read names from a text file

with open("data/names.txt") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())