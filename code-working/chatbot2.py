import spacy

nlp = spacy.load("en_core_web_sm")

users = {
    "ahmed": {"balance": 5000, "password": "1234", "transactions": ["+1000 (deposit)", "-200 (grocery)", "+500 (salary)"]},
    "sara": {"balance": 3200, "password": "5678", "transactions": ["-100 (shopping)", "+2000 (salary)", "-150 (utility bill)"]},
    "ali": {"balance": 1500, "password": "4321", "transactions": ["-50 (dinner)", "+1000 (freelance)", "-100 (utility bill)"]},
    "maryam": {"balance": 8000, "password": "8765", "transactions": ["+2000 (salary)", "-300 (shopping)", "+1000 (bonus)"]}
}

sessions = {}

def login(username):
    """Authenticate the user by verifying their password."""
    if username in users:
        password = input("Enter your password: ")
        if users[username]["password"] == password:
            sessions[username] = True
            return f"Welcome {username.capitalize()}!"
        return "Login failed. Incorrect password."
    return "Username not found."

def chatbot_response(user_input, username):
    doc = nlp(user_input.lower())
    
    if "balance" in user_input:
        if username in sessions and sessions[username]:
            return f"The balance of {username.capitalize()}'s account is ${users[username]['balance']}."
        else:
            return "Please log in first to check your balance."
    
    elif "transaction" in user_input or "recent" in user_input:
        if username in sessions and sessions[username]:
            return f"Recent transactions for {username.capitalize()}: {', '.join(users[username]['transactions'])}."
        else:
            return "Please log in first to view your recent transactions."
    
    return "I am a bank chatbot. You can ask me about your account balance or recent transactions."

def run_chatbot():
    print("Hello! I am your bank assistant. You can ask about your balance or transactions.")
    
    while True:
        username = input("Enter your username (or type 'exit' to quit): ").lower()
        
        if username == 'exit':
            print("System closed. Goodbye!")
            break
        
        login_response = login(username)
        print(login_response)
        
        if username in sessions and sessions[username]:
            while True:
                user_input = input(f"You ({username.capitalize()}): ").lower()
                
                if user_input == 'logout':
                    print(f"{username.capitalize()} logged out.")
                    sessions[username] = False
                    break
                
                response = chatbot_response(user_input, username)
                print("Bot: " + response)

run_chatbot()
