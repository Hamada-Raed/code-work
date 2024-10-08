from flask import Flask, request, jsonify

app = Flask(__name__)

banks = ["Bank A", "Bank B", "Bank C"]

def validate_data(data):
    required_fields = ['name', 'id', 'address', 'bank']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"{field} is required"
    
    if not data['id'].isdigit() or len(data['id']) != 10:
        return False, "ID must be 10 digits long."
    
    if data['bank'] not in banks:
        return False, "Selected bank is not available."
    
    return True, "Success!"

@app.route('/')
def welcome():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
    </head>
    <body>
        <h1>Welcome, open your bank account!</h1>
        <button onclick="location.href='/open_account_form';">Open Bank Account</button>
    </body>
    </html>
    '''

@app.route('/open_account_form')
def open_account_form():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Open Bank Account</title>
    </head>
    <body>
        <h1>Open Your Bank Account</h1>
        <form action="/open_account" method="POST">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name"><br><br>
            
            <label for="id">ID (10 digits):</label><br>
            <input type="text" id="id" name="id"><br><br>

            <label for="address">Address:</label><br>
            <input type="text" id="address" name="address"><br><br>

            <label for="bank">Bank:</label><br>
            <select id="bank" name="bank">
                <option value="Bank A">Bank A</option>
                <option value="Bank B">Bank B</option>
                <option value="Bank C">Bank C</option>
            </select><br><br>

            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    '''

@app.route('/open_account', methods=['POST'])
def open_account():
    data = {
        "name": request.form['name'],
        "id": request.form['id'],
        "address": request.form['address'],
        "bank": request.form['bank']
    }
    
    is_valid, message = validate_data(data)
    
    if is_valid:
        return jsonify({"status": "success", "message": "Account opened successfully!"})
    else:
        return jsonify({"status": "error", "message": message}), 400

@app.route('/banks', methods=['GET'])
def get_banks():
    return jsonify({'banks': banks})

if __name__ == "__main__":
    app.run(debug=True)
