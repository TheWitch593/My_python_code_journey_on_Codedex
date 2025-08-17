 

Gryffindor = 0
Hufflepuff = 0
Slytherin = 0
Ravenclaw = 0

# Q1
print("Q1) Do you like Dawn or Dusk?")
print("    1) Dawn")
print("    2) Dusk")
pointsQ1 = int(input("Enter your choice (1-2): "))

if pointsQ1 == 1:
    Gryffindor += 1
    Hufflepuff += 1
elif pointsQ1 == 2:
    Slytherin += 1
    Ravenclaw += 1
else:
    print("Wrong input.")

# Q2
print("Q2) When I'm dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
pointsQ2 = int(input("Enter your choice (1-4): "))

if pointsQ2 == 1:
    Hufflepuff += 2
elif pointsQ2 == 2:
    Slytherin += 2
elif pointsQ2 == 3:
    Ravenclaw += 2
elif pointsQ2 == 4:
    Gryffindor += 2
else:
    print("Wrong input.")

# Q3
print("Q3) Which kind of instrument most pleases your ear:")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
pointsQ3 = int(input("Enter your choice (1-4): "))

if pointsQ3 == 1:
    Slytherin += 4
elif pointsQ3 == 2:
    Hufflepuff += 4
elif pointsQ3 == 3:
    Ravenclaw += 4
elif pointsQ3 == 4:
    Gryffindor += 4
else:
    print("Wrong input.")

total_score = Gryffindor + Hufflepuff + Slytherin + Ravenclaw

highest = max(Gryffindor, Hufflepuff, Slytherin, Ravenclaw)

if highest == Gryffindor:
    house = "Gryffindor"
elif highest == Hufflepuff:
    house = "Hufflepuff"
elif highest == Slytherin:
    house = "Slytherin"
elif highest == Ravenclaw:
    house = "Ravenclaw"

print("\n✨ Quiz Results ✨")
print("🏠 Your house is:", house)