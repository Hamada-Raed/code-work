from flask import Flask, request, jsonify, render_template_string
 
app = Flask(__name__)
 
events = ["Concert", "Movie", "Theater"]
 
def validate_booking(data):
    required_fields = ['name', 'email', 'event']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"{field} is required."
    if "@" not in data['email'] or "." not in data['email']:
        return False, "Invalid email format."
    if data['event'] not in events:
        return False, "Selected event is not available."
    return True, "Booking successful!"
 
@app.route('/')
def welcome():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Event Booking</title>
</head>
<body>
<h1>Welcome to the Event Booking System</h1>
<button onclick="location.href='/book_ticket_form';">Book a Ticket</button>
</body>
</html>
    '''
 
@app.route('/book_ticket_form')
def book_ticket_form():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Book a Ticket</title>
</head>
<body>
<h1>Book Your Event Ticket</h1>
<form action="/book_ticket" method="POST">
<label for="name">Name:</label><br>
<input type="text" id="name" name="name"><br><br>
 
            <label for="email">Email:</label><br>
<input type="email" id="email" name="email"><br><br>
 
            <label for="event">Event:</label><br>
<select id="event" name="event">
<option value="Concert">Concert</option>
<option value="Movie">Movie</option>
<option value="Theater">Theater</option>
</select><br><br>
 
            <button type="submit">Submit</button>
</form>
</body>
</html>
    '''
 
@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    data = {
        "name": request.form['name'],
        "email": request.form['email'],
        "event": request.form['event']
    }
    is_valid, message = validate_booking(data)
    if is_valid:
        return jsonify({"status": "success", "message": "Your ticket has been booked!"})
    else:
        return jsonify({"status": "error", "message": message}), 400
 
@app.route('/events', methods=['GET'])
def get_events():
    return jsonify({'events': events})
 
if __name__ == "__main__":
    app.run(debug=True)