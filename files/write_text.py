# Write 5 names to a text file

file = open('data/names.txt', 'a')

for i in range(5):
    name = input("Name: ")
    file.write(name + "\n")