from google import genai

while True and tries < 10: # limit to 10 tries
    # increment tries counter
    tries += 1

    print("\nGemini: How can I assist you? \n")

    # The user answer
    answer = input("You: ")
    
    # The gemini response
    response = client.models.generate_content(
    model="gemini-1.5-flash", contents=answer
    )

    print("\nGemini: " + response.text)

    # ask if the user wants to continue
    print("Gemini: Do you want to ask something else? (yes/no)")
    ans = input("\n You: ")
    # Based on the user answer, continue or break the loop
    if ans.lower() != "yes":
        break
    else:
        continue
else:
    # If the user reaches the maximum number of tries, 
    # they will be informed
    print("\nGemini: You've reached the maximum number of tries. Goodbye!")

# If the user types "exit", the program will terminate
if answer == "exit":
   print("\nGemini: Goodbye!")
   exit()

