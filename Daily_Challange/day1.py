def wordle_guess(secret, guess):
  # Write code below 💖
  matches = 0 # Initialize a variable to count the number of matches

  for i in range(len(secret)): # Loop through each character in the secret word 
    if secret[i]==guess[i]: # If the character at the current index in the secret word matches the character at the same index in the guess word, increment the matches count
      matches+=1
  return matches