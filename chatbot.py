print("Welcome to Customer Support Chatbot")
print("Type 'bye' to exit\n")

while True:

    user = input("You: ").lower()

    if user == "hello" or user == "hi":

        print("Bot: Hello! How can I help you?")

    elif "price" in user:

        print("Bot: Our product price starts from ₹500.")

    elif "delivery" in user:

        print("Bot: Delivery takes 3 to 5 days.")

    elif "refund" in user:

        print("Bot: Refund is available within 7 days.")

    elif "contact" in user:

        print("Bot: You can contact us at support@gmail.com")

    elif user == "bye":

        print("Bot: Thank you! Have a nice day.")
        break

    else:

        print("Bot: Sorry, I did not understand.")
