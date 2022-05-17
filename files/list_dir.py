import os


contents = os.listdir('data')

for entry in contents:
    if os.path.isdir('data/' + entry):
        print("d " + entry)
    else:
        print("f " + entry)