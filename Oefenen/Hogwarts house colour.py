gryffindor = "Scarlet and Yellow"
hufflepuff = "Yellow and Black"
ravenlaw = "Blue and Bronze"
slytherin = "Green and Silver"

houseQuestion = input("Which house are you in?")

if houseQuestion == "gryffindor":
    print("Your house colours are:",gryffindor)
elif houseQuestion == "hufflepuff":
    print("Your house colours are:",hufflepuff)
elif houseQuestion == "ravenclaw":
    print("Your house colours are:",ravenlaw)
elif houseQuestion == "slytherin":
    print("Your house colours are:",slytherin)
else:
    print("No house given.")