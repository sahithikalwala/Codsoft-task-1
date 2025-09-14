def simple_chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()  
        
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I help you today?")
            
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! Thank you for asking.")
            
        elif "your name" in user_input:
            print("Chatbot: I'm called SimpleBot. What's your name?")
            
        elif "weather" in user_input:
            print("Chatbot: I can't check real-time weather, but I hope it's nice where you are!")
            
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome!")
            
        else:
            print("Chatbot: Sorry, I don't understand that. Can you rephrase?")
simple_chatbot()
