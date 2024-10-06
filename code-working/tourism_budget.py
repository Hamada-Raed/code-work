from flask import Flask, render_template_string, request
app = Flask(__name__)
features = {
   "historical_info": {"name": "Providing historical information about archaeological sites", "cost": 5000},
   "tourism_services": {"name": "Showcasing tourism services, activities, and events", "cost": 7000},
   "communication_channels": {"name": "Offering direct communication channels with service providers", "cost": 4000},
   "emergency_info": {"name": "Providing emergency contact information", "cost": 2000},
   "local_needs": {"name": "Catering to the needs of both local and foreign visitors", "cost": 3000},
}
TOTAL_BUDGET = 22000
WARNING_LIMIT = 10000
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tourism Platform Cost Calculator</title>
<style>
       body {
           background-color: {{ background_color }};
           color: white;
           font-family: Arial, sans-serif;
           padding: 20px;
       }
       h1 {
           text-align: center;
       }
       form {
           max-width: 600px;
           margin: auto;
       }
       .message {
           font-weight: bold;
       }
</style>
</head>
<body>
<h1>Tourism Platform Cost Calculator</h1>
<form method="POST">
       {% for key, feature in features.items() %}
<div>
<input type="checkbox" name="features" value="{{ key }}" id="{{ key }}">
<label for="{{ key }}">{{ feature.name }} (Cost: ${{ feature.cost }})</label>
</div>
       {% endfor %}
<button type="submit">Calculate Total Cost</button>
</form>
<h2>Total Cost: ${{ total_cost }}</h2>
   {% if messages %}
<div class="message">
           {% for msg in messages %}
<p>{{ msg }}</p>
           {% endfor %}
</div>
   {% endif %}
</body>
</html>
"""
@app.route('/', methods=['GET', 'POST'])
def index():
   total_cost = 0
   selected_features = []
   if request.method == 'POST':
       selected_features = request.form.getlist('features')
       total_cost = sum(features[feature]['cost'] for feature in selected_features)
   background_color = 'green' if total_cost <= WARNING_LIMIT else 'red'
   messages = []
   if total_cost > WARNING_LIMIT:
       messages.append("Warning: The cost has exceeded the $10,000 budget limit.")
   if total_cost > TOTAL_BUDGET:
       messages.append("Alert: The total cost has exceeded the overall budget of $22,000.")
   return render_template_string(HTML_TEMPLATE, features=features, total_cost=total_cost,
                                  background_color=background_color, messages=messages)
if __name__ == '__main__':
   app.run(debug=True)
