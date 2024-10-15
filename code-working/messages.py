# Mock User Database
user_database = {"user1", "user2", "user3"}

# Mock Message Class
class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content

def handle_message(message):
    """
    Handles an incoming message and routes it to the appropriate recipient.
    
    Args:
        message (Message): The incoming message object.
    
    Returns:
        None
    """
    try:
        validate_message(message)
        route_message(message)
    except Exception as e:
        handle_error(message, str(e))


def validate_message(message):
    """
    Validates the sender and recipient of the message.
    
    Args:
        message (Message): The incoming message object.
    
    Raises:
        ValueError: If the sender or recipient is invalid.
    """
    if message.sender not in user_database and message.sender != "admin":
        raise ValueError("Sender not found")
    if message.recipient not in user_database and message.recipient != "all":
        raise ValueError("Recipient not found")


def route_message(message):
    """
    Routes the message to the appropriate recipient.
    
    Args:
        message (Message): The incoming message object.
    
    Returns:
        None
    """
    if message.sender == "admin":
        handle_admin_message(message)
    else:
        send_direct_message(message)


def handle_admin_message(message):
    """
    Handles a message sent by the admin.
    
    Args:
        message (Message): The incoming message object.
    
    Returns:
        None
    """
    if message.recipient == "all":
        broadcast_message(message)
    else:
        send_direct_message(message, recipient=message.recipient)


def broadcast_message(message):
    """
    Broadcasts a message to all users.
    
    Args:
        message (Message): The incoming message object.
    
    Returns:
        None
    """
    for user in user_database:
        send_direct_message(message, recipient=user)


def send_direct_message(message, recipient=None):
    """
    Sends a direct message to a recipient.
    
    Args:
        message (Message): The incoming message object.
        recipient (str): The recipient's username. If None, it should default to message.recipient.
    
    Returns:
        None
    """
    if recipient is None:
        recipient = message.recipient
    print(f"Sent message from {message.sender} to {recipient}: {message.content}")


def send_error_message(message, error_text):
    """
    Sends an error message to the sender.
    
    Args:
        message (Message): The incoming message object.
        error_text (str): The error message text.
    
    Returns:
        None
    """
    print(f"Error to {message.sender}: {error_text}")


def handle_error(message, error_text):
    """
    Handles an error that occurred during message processing.
    
    Args:
        message (Message): The incoming message object.
        error_text (str): The error message text.
    
    Returns:
        None
    """
    send_error_message(message, error_text)

# Example Usage
message1 = Message(sender="user1", recipient="user2", content="Hello User 2!")
handle_message(message1)

message2 = Message(sender="admin", recipient="all", content="System maintenance at 3 PM.")
handle_message(message2)

message3 = Message(sender="user4", recipient="user2", content="Hi!")  # This will raise an error
handle_message(message3)