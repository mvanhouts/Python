
# path where files are stored (you'll need to change this)
file_path = "C:\\Users\\mhouts\OneDrive - Centric\\Documents\\Portfolio\\Python\\Oefenen\\Grandprix\\"

# read first file into a list
with open(file_path + "Grand Prix 2016.csv", 'r') as gp_2016:

    # read all lines into list
    grand_prix_2016 = [line.split(",")[1] for line in gp_2016.read().splitlines()]

# read second file into a list
with open(file_path + "Grand Prix 2017.csv", 'r') as gp_2017:

    # read all lines into list
    grand_prix_2017 = [line.split(",")[1] for line in gp_2017.read().splitlines()]

# show results so far
#print(grand_prix_2016)
#print(grand_prix_2017)

set2016 = set(grand_prix_2016)
set2017 = set(grand_prix_2017)

notInBoth = set2016 ^ set2017

print(notInBoth)

for item in notInBoth:
    if item in set2016:
        print(item,"belongs to 2016 race")
    elif item in set2017:
        print(item,"belongs to 2017 race")