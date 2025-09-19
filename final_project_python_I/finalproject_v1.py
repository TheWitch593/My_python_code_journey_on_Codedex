from google import genai
import time

client = genai.Client()

tries = 0

while True and tries < 10: # limit to 10 tries
    tries += 1
    print("\nGemini: How can I assist you? \n")

    # The user answer
    answer = input("You: ")
    
    # The gemini response
    response = client.models.generate_content(
    model="gemini-1.5-flash", contents=answer
    )

    print("\nGemini: " + response.text)

    print("Gemini: Do you want to ask something else? (yes/no)")
    ans = input("\nYou: ")
    if ans.lower() != "yes":
        break
else:
    print("\nGemini: You've reached the maximum number of tries. Goodbye!")



