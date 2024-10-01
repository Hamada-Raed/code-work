accounts = {
    "Ahmad" : 5000, 
    "Ali" : 10000, 
    "Sara" : 500, 
    "Nehal" : 5000, 
    "Hamada" : 5000, 
}

def chatbot_response(user_input): 
    user_input = user_input.lower()
    
    if "balance" in user_input: 
        for name in accounts: 
            if name in user_input: 
                return f"The balance of {name.capitalize()}'s account is {accounts[name]}."
            
        return "Sorry, I couldn't find you account. Please provide a valid name." 
    
    return "I am a simple bank bot. You can ask me about your account balance. "

def run_chatbot():
    print('Hello! I am your bank assistant. Ask me about your account balance.')
    
    while True: 
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("System Closed. Goodbye!")
            break 
        
        response = chatbot_response(user_input) 
        print("Bot: " + response)
        
run_chatbot()