user_database = {"user1", "user2", "user3"}

class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content

def handle_message(message):
    try:
        validate_message(message)
        route_message(message)
    except Exception as e:
        handle_error(message, str(e))


def validate_message(message):
    if message.sender not in user_database and message.sender != "admin":
        raise ValueError("Sender not found")
    if message.recipient not in user_database and message.recipient != "all":
        raise ValueError("Recipient not found")


def route_message(message):
    if message.sender == "admin":
        handle_admin_message(message)
    else:
        send_direct_message(message)


def handle_admin_message(message):
    if message.recipient == "all":
        broadcast_message(message)
    else:
        send_direct_message(message, recipient=message.recipient)


def broadcast_message(message):
    for user in user_database:
        send_direct_message(message, recipient=user)


def send_direct_message(message, recipient=None):
    if recipient is None:
        recipient = message.recipient
    print(f"Sent message from {message.sender} to {recipient}: {message.content}")


def send_error_message(message, error_text):
    print(f"Error to {message.sender}: {error_text}")


def handle_error(message, error_text):
    send_error_message(message, error_text)

message1 = Message(sender="user1", recipient="user2", content="Hello User 2!")
handle_message(message1)

message2 = Message(sender="admin", recipient="all", content="System maintenance at 3 PM.")
handle_message(message2)

message3 = Message(sender="user4", recipient="user2", content="Hi!") 