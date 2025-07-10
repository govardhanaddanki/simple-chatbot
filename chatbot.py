
---

# 🐍 `chatbot.py`

```python
# Simple Question-Answer Chatbot
# Filename: chatbot.py

def chatbot(user_input):
    # convert input to lowercase for easier matching
    question = user_input.lower()

    # define simple question-answer pairs
    if question == "what is your name?":
        return "I am ChatBot!"
    elif question == "how are you?":
        return "I am just a bot, but I am doing fine!"
    elif question == "what can you do?":
        return "I can answer a few simple questions."
    elif question == "who created you?":
        return "I was created by a programmer as a demo project."
    elif question == "bye":
        return "Goodbye! Have a great day!"
    else:
        return "I don't understand that question. Please ask something else."

def main():
    print("Welcome! Ask me a question. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot(user_input)
        print("Bot:", response)
        if user_input.lower() == "bye":
            break

if __name__ == "__main__":
    main()
