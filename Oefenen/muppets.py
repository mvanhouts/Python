file_path = "C:\\Users\\mhouts\OneDrive - Centric\\Documents\\Portfolio\\Python\\Oefenen\\muppets.csv"

with open(file_path, 'r') as f:
    listNames = f.read().splitlines()
f.close()

for line in listNames:
    muppetObject = line.split(",")
    muppet, animal, colour = muppetObject
    print(f"{muppet} ({animal} {colour})")