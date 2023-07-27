file_path = "C:\\Users\\mhouts\OneDrive - Centric\\Documents\\Portfolio\\Python\\Oefenen\\Details.txt"

with open(file_path, 'w+') as f:
    f.write("File succesfully created!\n\n")
    f.write("My name is Max\n")
    f.write("I live in NL\n")
    f.write("I'm an avid painter")
f.close()

with open(file_path, 'r') as r:
    print(r.read())