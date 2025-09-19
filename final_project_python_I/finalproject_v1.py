from google import genai
import time

# Set your API key here if not using environment variable
# genai.configure(api_key="YOUR_API_KEY")
client = genai.Client()

tries = 0

while tries < 10:  # limit to 10---------------- tries
    tries += 1
    print("\nGemini: How can I assist you? \n")

    # The user answer
    answer = input("You: ")

    # If the user types "exit", the program will terminate
    if answer.lower() == "exit":
        print("\nGemini: Goodbye!")
        exit()

    # The gemini response with error handling and retry
    response = None
    for attempt in range(3):  # try up to 3 times if there's an error
        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash", contents=answer
            )
            print("\nGemini: " + response.text)
            break  # stop retrying if successful
        except Exception as e:
            print("\nGemini: Oops! Something went wrong while contacting the Gemini API.")
            print("Error details:", e)
            print(f"Gemini: Retrying... Attempt {attempt+1} of 3.")
            time.sleep(1)  # wait before retrying

    if response is None:
        print("\nGemini: Sorry, I couldn’t process your request after 3 attempts.")

    # Ask if the user wants to continue
    print("Gemini: Do you want to ask something else? (yes/no)")
    ans = input("\nYou: ")
    if ans.lower() != "yes":
        print("\nGemini: Goodbye!")
        break

else:
 print("\nGemini: You've reached the maximum number of tries. Goodbye!")
