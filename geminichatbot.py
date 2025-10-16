import google.generativeai as genai

GEMINI_API_KEY = "YOUR_API_KEY"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

print("Gemini Chatbot is ready! Type 'quit' to exit.")
print("=" * 50)

while True:
    user_input = input("You : ")

    if not user_input.strip():
        print("Gemini: Please provide some input.")
        continue

    if user_input.lower() == "quit":
        print("\nGoodbye, thank you for chatting with Gemini.")
        break

    try:
        response = chat.send_message(user_input, stream=True)
        print("Gemini : ", end="")
        for chunk in response:
            print(chunk.text, end="")
        print("\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("\n")