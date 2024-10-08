from flask import Flask, request, render_template_string
 
app = Flask(__name__)
 
@app.route('/')
def travel_organizer():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Multi-Destination Travel Organizer</title>
<style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }
            .container {
                width: 80%;
                margin: 20px auto;
                background-color: white;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            h1 {
                text-align: center;
                color: #333;
            }
            form {
                display: flex;
                flex-direction: column;
                gap: 10px;
            }
            label {
                margin-top: 10px;
                font-weight: bold;
            }
            input {
                padding: 10px;
                margin-top: 5px;
                border: 1px solid #ccc;
                border-radius: 4px;
                width: 100%;
            }
            button {
                padding: 10px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                margin-top: 20px;
            }
            button:hover {
                background-color: #0056b3;
            }
            .tour-visual {
                margin-top: 30px;
                text-align: center;
            }
            .path {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 20px;
            }
            .destination {
                background-color: #007bff;
                color: white;
                padding: 10px;
                border-radius: 4px;
                width: 100px;
                text-align: center;
            }
            .arrow {
                margin: 0 20px;
                font-size: 20px;
                color: #333;
            }
            .time {
                font-size: 14px;
                color: #555;
            }
</style>
</head>
<body>
<div class="container">
<h1>Multi-Destination Travel Organizer</h1>
<form id="tourForm">
<label for="tour_name">Tour Name:</label>
<input type="text" id="tour_name" name="tour_name" required>
 
                <label for="destinations">Destinations (separate by commas):</label>
<input type="text" id="destinations" name="destinations" required placeholder="e.g., City1, City2, City3">
 
                <label for="travel_times">Travel Times (in hours, separate by commas):</label>
<input type="text" id="travel_times" name="travel_times" required placeholder="e.g., 2, 5, 3">
 
                <button type="submit">Create Travel Path</button>
</form>
 
            <div class="tour-visual" id="tourVisual"></div>
</div>
 
        <script>
            document.getElementById('tourForm').addEventListener('submit', function(e) {
                e.preventDefault();
                const tourName = document.getElementById('tour_name').value;
                const destinations = document.getElementById('destinations').value.split(',');
                const travelTimes = document.getElementById('travel_times').value.split(',');
 
                let visualHtml = `<h2>${tourName}</h2><div class="tour-paths">`;
 
                for (let i = 0; i < destinations.length - 1; i++) {
                    visualHtml += `
<div class="path">
<div class="destination">${destinations[i].trim()}</div>
<div class="arrow">➔</div>
<div class="time">${travelTimes[i].trim()} hours</div>
<div class="destination">${destinations[i+1].trim()}</div>
</div>
                    `;
                }
 
                visualHtml += `</div>`;
                document.getElementById('tourVisual').innerHTML = visualHtml;
            });
</script>
</body>
</html>
    '''
 
if __name__ == "__main__":
    app.run(debug=True)