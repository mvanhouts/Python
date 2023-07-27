import os

filePath = "C:\\Users\\mhouts\OneDrive - Centric\\Documents\\Portfolio\\Python\\Oefenen\\Grandprix"

entries = os.scandir(filePath)

print("Files and Directories in '% s':" % filePath)
for entry in entries:
    if entry.is_dir() or entry.is_file():
        flexFilePath = filePath + "\\" + entry.name
        with open(flexFilePath, 'r') as gp_2016:
            grand_prix_2016 = [line.split(",")[1] for line in gp_2016.read().splitlines()]
