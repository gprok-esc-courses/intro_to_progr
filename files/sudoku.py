import random
import csv
import os
from datetime import datetime

# sudoku file retrieved from here:
# https://www.kaggle.com/datasets/bryanpark/sudoku

file = open("data/sudoku.csv")
csv_file = csv.reader(file, delimiter=',')
rnd = random.randint(1, 1000001)
print("Random line: " + str(rnd))

puzzle = ''
current = ''
solution = ''

counter = 0
for row in csv_file:
    if counter == rnd:
        puzzle = row[0]
        current = row[0]
        solution = row[1]
        break
    counter += 1

print(puzzle)
print(solution)

def clear_screen():
    if os.name == 'posix':
        a = os.system('clear')
    else:
        a = os.system('cls')

start = datetime.now()
while True:
    counter = 1
    print(solution)
    for ch in current:
        if ch == '0':
            print('-', end=' ')
        else:
            print(ch, end=' ')
        if counter % 3 == 0:
            print('  ', end='')
        if counter % 9 == 0:
            print()
        if counter % 27 == 0:
            print()
        counter += 1

    row = int(input("Row: "))
    col = int(input("Col: "))
    val = input("Val: ")

    pos = (row-1) * 9 + (col-1)

    # check if val is correct
    if puzzle[pos] != '0':
        print("ERROR: Can't play here")
    elif solution[pos] != val:
        print("ERROR: Wrong value")
    else:
        current = current[:pos] + val + current[pos+1:]

    # check if found
    if current == solution:
        t = datetime.now() - start
        print("Congratulations!!!!! Solved in " + str(t))
        break


