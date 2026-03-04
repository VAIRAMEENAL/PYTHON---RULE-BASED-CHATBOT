# Rule-Based Chatbot
print("Bot: Hello! I am FunBot 🤖")
print("Bot: Type 'exit' to stop the chat.\n")

while True:
    user = input("You: ").lower()

    if user == "exit" or user == "bye":
        print("Bot: Goodbye! Have a nice day 😊")
        break

    elif "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user:
        print("Bot: I am fine! Thank you for asking 😊")

    elif "name" in user:
        print("Bot: My name is FunBot 🤖")

    elif "python" in user:
        print("Bot: Python is a programming language used for AI, web development, and data science.")

    elif "sql" in user:
        print("Bot: SQL is used to store, manage and retrieve data from databases.")

    elif "joke" in user:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs! 😄")

    elif "html" in user:
        print("Bot: HTML is HyperText Markup Language, which creates a structure of a webpage.")

    elif "file handling" in user:
        print("Bot: File handling in python is used to create, read, write, append and delete files. it allows programs to store data permanently.")

    elif "mode" in user:
        print("Bot: Modes of file handling are : 1. read(r)  2.write(w)  3.append(a) ")

    elif "class" in user:
        print("Bot: A class is a blueprint for creating the objects.")

    elif "object" in user:
        print("Bot: An object is an instance of a class.")

    elif "tkinter" in user:
        print("Bot: Tkinter is a python's built in library used to create GUI applications (windows, buttons, textboxes).")

    elif "django" in user:
        print("Bot: Django is a high level python web framework used to build secure,scalable and fast web applications. ")

    elif "thank" in user:
        print("Bot: You're welcome! 😊")

    else:
        print("Bot: Sorry, I don't understand that yet.")