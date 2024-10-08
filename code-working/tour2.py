from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
# In-memory storage for tours and notifications

tours = []

notifications = []
 
# Function to validate the tour data

def validate_tour_data(data):

    required_fields = ['tour_name', 'location', 'start_date', 'end_date', 'itinerary']

    for field in required_fields:

        if field not in data or not data[field]:

            return False, f"{field} is required."
 
    if data['start_date'] > data['end_date']:

        return False, "Start date cannot be after end date."

    return True, "Tour successfully organized!"
 
# Function to validate notifications

def validate_notification(data):

    if 'message' not in data or not data['message']:

        return False, "Notification message is required."

    return True, "Notification sent!"
 
@app.route('/')

def tour_organizer():

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Advanced Tour Organizer</title>
<style>

            body {

                font-family: Arial, sans-serif;

                background-color: #f4f4f4;

                padding: 0;

                margin: 0;

            }

            .container {

                width: 60%;

                margin: 50px auto;

                padding: 20px;

                background-color: #fff;

                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);

            }

            h1 {

                text-align: center;

                color: #333;

            }

            form {

                display: flex;

                flex-direction: column;

            }

            label {

                margin-top: 10px;

                color: #333;

            }

            input, textarea, select {

                padding: 10px;

                margin-top: 5px;

                border: 1px solid #ccc;

                border-radius: 4px;

            }

            button {

                margin-top: 20px;

                padding: 10px;

                background-color: #28a745;

                color: white;

                border: none;

                border-radius: 4px;

                cursor: pointer;

            }

            button:hover {

                background-color: #218838;

            }

            .message {

                margin-top: 20px;

                padding: 15px;

                border-radius: 4px;

                text-align: center;

            }

            .success {

                background-color: #d4edda;

                color: #155724;

            }

            .error {

                background-color: #f8d7da;

                color: #721c24;

            }
</style>
</head>
<body>
<div class="container">
<h1>Advanced Tour Organizer</h1>
<form id="tourForm">
<label for="tour_name">Tour Name:</label>
<input type="text" id="tour_name" name="tour_name" required>
 
                <label for="location">Location:</label>
<input type="text" id="location" name="location" required>
 
                <label for="start_date">Start Date:</label>
<input type="date" id="start_date" name="start_date" required>
 
                <label for="end_date">End Date:</label>
<input type="date" id="end_date" name="end_date" required>
 
                <label for="itinerary">Itinerary (separate events by comma):</label>
<textarea id="itinerary" name="itinerary" rows="4"></textarea>
 
                <button type="submit">Organize Tour</button>
</form>
 
            <div class="message" id="message"></div>
 
            <h2>Send Notification to Participants</h2>
<form id="notificationForm">
<label for="message">Notification Message:</label>
<textarea id="message" name="message" rows="3" required></textarea>
<button type="submit">Send Notification</button>
</form>
 
            <div class="message" id="notificationMessage"></div>
</div>
 
        <script>

            // Tour form submission

            document.getElementById('tourForm').addEventListener('submit', function(e) {

                e.preventDefault();

                const formData = new FormData(this);

                const tourData = {

                    tour_name: formData.get('tour_name'),

                    location: formData.get('location'),

                    start_date: formData.get('start_date'),

                    end_date: formData.get('end_date'),

                    itinerary: formData.get('itinerary').split(',')

                };

                fetch('/organize_tour', {

                    method: 'POST',

                    headers: {

                        'Content-Type': 'application/json'

                    },

                    body: JSON.stringify(tourData)

                })

                .then(response => response.json())

                .then(data => {

                    const messageDiv = document.getElementById('message');

                    if (data.status === 'success') {

                        messageDiv.className = 'message success';

                        messageDiv.textContent = data.message;

                    } else {

                        messageDiv.className = 'message error';

                        messageDiv.textContent = data.message;

                    }

                })

                .catch(error => console.error('Error:', error));

            });
 
            // Notification form submission

            document.getElementById('notificationForm').addEventListener('submit', function(e) {

                e.preventDefault();

                const formData = new FormData(this);

                const notificationData = {

                    message: formData.get('message')

                };
 
                fetch('/send_notification', {

                    method: 'POST',

                    headers: {

                        'Content-Type': 'application/json'

                    },

                    body: JSON.stringify(notificationData)

                })

                .then(response => response.json())

                .then(data => {

                    const messageDiv = document.getElementById('notificationMessage');

                    if (data.status === 'success') {

                        messageDiv.className = 'message success';

                        messageDiv.textContent = data.message;

                    } else {

                        messageDiv.className = 'message error';

                        messageDiv.textContent = data.message;

                    }

                })

                .catch(error => console.error('Error:', error));

            });
</script>
</body>
</html>

    '''
 
@app.route('/organize_tour', methods=['POST'])

def organize_tour():

    data = request.get_json()

    is_valid, message = validate_tour_data(data)

    if is_valid:

        tours.append(data)

        return jsonify({"status": "success", "message": "Tour organized successfully!"})

    else:

        return jsonify({"status": "error", "message": message}), 400
 
@app.route('/send_notification', methods=['POST'])

def send_notification():

    data = request.get_json()

    is_valid, message = validate_notification(data)

    if is_valid:

        notifications.append(data)

        return jsonify({"status": "success", "message": "Notification sent!"})

    else:

        return jsonify({"status": "error", "message": message}), 400
 
if __name__ == "__main__":

    app.run(debug=True)

 