
file = open('data/titanic.csv')

lines = file.readlines()

for line in lines:
    tokens = line.split(',')
    print(tokens)