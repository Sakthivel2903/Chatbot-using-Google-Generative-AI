# Chatbot-using-Google-Generative-AI
Here’s a clear and well-structured **project description** for your code 👇

---

## 🧠 **Gemini Chatbot using Google Generative AI (Python)**

### 📋 **Project Description**

This project demonstrates how to build an **interactive chatbot** using **Google’s Generative AI (Gemini API)** in Python.
The chatbot allows users to have real-time text-based conversations with Google’s **Gemini 1.5 Flash model** directly from the command line.

---

### 🚀 **Features**

* 💬 **Interactive Chat Loop:** Users can continuously chat with the AI until they type `quit`.
* ⚡ **Streaming Responses:** The AI’s reply is displayed in real-time, simulating natural conversation flow.
* 🧩 **Error Handling:** Handles invalid input and exceptions gracefully.
* 🧠 **Memory Context:** The chat maintains conversation history for a more natural dialogue experience.

---

### 🛠️ **How It Works**

1. The script connects to Google’s **Generative AI API** using the provided **API key**.
2. It initializes the **Gemini 1.5 Flash model**, which is optimized for fast and intelligent text generation.
3. The program enters a loop where it waits for user input.
4. The chatbot sends the input to Gemini and streams the generated response back to the console.
5. The loop continues until the user types **"quit"**.

---

### 🧩 **Code Overview**

| Section                                             | Description                                             |
| --------------------------------------------------- | ------------------------------------------------------- |
| `import google.generativeai as genai`               | Imports Google’s Generative AI SDK.                     |
| `genai.configure(api_key=GEMINI_API_KEY)`           | Authenticates with your API key.                        |
| `model = genai.GenerativeModel('gemini-1.5-flash')` | Initializes the Gemini model.                           |
| `chat = model.start_chat(history=[])`               | Starts a new chat session with empty history.           |
| `while True:`                                       | Runs an infinite chat loop.                             |
| `chat.send_message(user_input, stream=True)`        | Sends the user’s message and streams Gemini’s response. |

---

### ⚙️ **Setup Instructions**

1. Install the Google Generative AI SDK:

   ```bash
   pip install google-generativeai
   ```
2. Replace `"YOUR_API_KEY"` with your actual **Gemini API key**.
3. Run the Python script:

   ```bash
   python gemini_chatbot.py
   ```
4. Start chatting! Type your queries and get instant AI responses.
   Type **`quit`** to exit.

---

### 🧠 **Example Interaction**

```
Gemini Chatbot is ready! Type 'quit' to exit.
==================================================

You : Hello Gemini!
Gemini : Hi there! How can I help you today?

You : Explain what AI is.
Gemini : Artificial Intelligence is the simulation of human intelligence in machines...
```

---

### 🎯 **Use Cases**

* Educational chatbot for learning about AI.
* Personal assistant in the terminal.
* Testing Gemini API integrations before embedding in web apps.

---

Would you like me to format this as a **README.md file** (GitHub-ready)?
