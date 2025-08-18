
import random

symbols = ['🍒',' 🍇', '🍉', '7️⃣']

def play():
 while True:
  results = random.choices(symbols, k=3)
  print(f"\n{results[0]} | {results[1]} | {results[2]}")
  if results == ['7️⃣','7️⃣','7️⃣']:
    print( "Jackpot! 💰")
  else:
    print("Thanks for playing!")
  continues = input("\nDo you want to continue: Y/N ")        
  if continues.upper() == "N":        
     print("\nGoodbye")        
     break

play()

