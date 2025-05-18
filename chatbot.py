def rule_based_chatbot():
    print("Chatbot: Hello! I'm your chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi! How are you?")
                
                
        elif "how are you" in user_input:
            print("Chatbot: I'm doing great, what about you? ")
            
        elif "your name" in user_input:
            print("Chatbot: My name is Chatbot, your AI Assistent!")
            
        elif "love" in user_input:
            print("Chatbot: Love is beatiful feeling, especially when it's from you!")
            
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Take care. Let's meet in the next time.")
            break
        
        else:
            print("Chatbot: Sorry. I don't have a rule for that. Please ask something else.")
            
rule_based_chatbot()