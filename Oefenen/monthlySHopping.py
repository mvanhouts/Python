import os

filePath = "C:\\Users\\mhouts\OneDrive - Centric\\Documents\\Portfolio\\Python\\Oefenen\\Grandprix"

entries = os.scandir(filePath)

print("Files and Directories in '% s':" % filePath)
for entry in entries:
    if entry.is_dir() or entry.is_file():
        print(entry.name)
