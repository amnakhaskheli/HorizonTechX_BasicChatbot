import random

print("================================")
print("      Welcome to PyChat!")
print("================================")
print("Bot: Hello! I am your Python chatbot.")
print("Bot: You can talk to me about studies, hobbies, and more.")
print("Bot: Type 'bye' or 'q' to exit.\n")

while True:
    message = input("You: ").lower().strip()

    if message in ("bye", "q"):
        print("Bot: Goodbye! Have a great day!")
        break

    elif "hello" in message or "hi" in message:
        replies = [
            "Hello! How are you?",
            "Hi! Nice to talk to you.",
            "Hey! How can I help you?"
        ]
        print("Bot:", random.choice(replies))

    elif "how are you" in message:
        print("Bot: I am fine! Thanks for asking.")

    elif "name" in message:
        print("Bot: My name is PyChat.")

    elif "study" in message or "student" in message:
        print("Bot: Keep learning and never give up!")

    elif "python" in message:
        print("Bot: Python is a beginner-friendly programming language.")

    elif "hobby" in message:
        print("Bot: I enjoy chatting! What is your hobby?")

    elif "happy" in message:
        print("Bot: That's wonderful! Keep smiling.")

    elif "sad" in message:
        print("Bot: I hope things get better for you.")

    elif "thank" in message:
        print("Bot: You're welcome!")

    elif "help" in message:
        print("Bot: You can ask about Python, studies, hobbies, or greetings.")

    else:
        replies = [
            "That's interesting! Tell me more.",
            "I am still learning. Can you say that differently?",
            "I see! What else would you like to talk about?",
            "Sorry, I don't understand that yet."
        ]
        print("Bot:", random.choice(replies))