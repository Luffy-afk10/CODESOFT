#!/usr/bin/env python
# coding: utf-8

# In[1]:


class RuleBasedChatbot:
    def __init__(self):
        # Define your rules here
        self.rules = {
            "hi": "Hello! How can I assist you today?",
            "how are you?": "I'm just a bot, but thanks for asking!",
            "bye": "Goodbye! Have a great day!",
            "can you help me?" : " Yes What i can do for you",
            "thank you" : " Your Welcome" 
            # Add more rules as needed
        }

    def respond(self, user_input):
        user_input = user_input.lower()  # Convert user input to lowercase for case-insensitive matching

        # Check if there's a matching rule
        if user_input in self.rules:
            return self.rules[user_input]
        else:
            return "I'm sorry, I didn't understand that."

if __name__ == "__main__":
    # Instantiate the chatbot
    chatbot = RuleBasedChatbot()

    # Main interaction loop
    while True:
        # Get user input
        user_input = input("You: ")

        # Check for exit condition
        if user_input.lower() == 'exit':
            print("Chat ended.")
            break

        # Get response from chatbot and print it
        response = chatbot.respond(user_input)
        print("Bot:", response)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




