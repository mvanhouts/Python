import csv
import os
print (os.getcwd())
with open("C:/Users/mvhouts/LocalPythonFiles/ContactlijstMarcServaes") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)