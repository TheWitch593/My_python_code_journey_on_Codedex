import random
tries = 0 #contor
while True and tries != 2: #Jocul continue atata timp cat 
                           #incercarile sunt dif de contor
 
 print("\nWelcome, let's play a game of rock,paper,scrissor")
 print("\nYou will play this game with the computer")

 calculator = ["✊","✂️","📄"] #option

 print("\nLet's start the game, is your turn")
 user = input("\nPlease choose: ")
 userchoice = ""
 
 #Transform the letter into an emoji 
 if user == "r":
    print("The user chose ✊")
    userchoice = "✊"
 elif user == "p":
    print("The user chose 📄")
    userchoice = "📄"
 elif user == "s":
    print("The user chose ✂️")
    userchoice = "✂️"
 else:
    print("Invalid choice")

#Computer turn
 comp1 = random.choice(calculator)
 computerchoice = print(f"\nThe computer choose {comp1}")

#Dictionary with all the possible outcome of the game
 outcome = {
   ("✊","✊"): "tie",
   ("📄","📄"): "tie",
   ("✂️","✂️"): "tie",
   ("✊","✂️"): "user",
   ("📄","✊"): "user",
   ("✂️","📄"): "user",
   ("✂️","✊"): "computer",
   ("✊","📄"): "computer",
   ("📄","✂️"): "computer",
}

#Winner announce 
 if not userchoice:
    print("\nNo valid user choice; cannot determine winner.")
 else:
    result = outcome.get((userchoice, comp1))
    if result == "tie":
        print("\nIt's a tie!\n")
    elif result == "user":
        print("\nYou win!\n")
    elif result == "computer":
        print("\nComputer wins!\n")
    else:
        print("\nCould not determine winner.\n")

 tries += 1 #contor iteratiom
