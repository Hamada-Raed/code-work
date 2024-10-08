from flask import Flask, request, jsonify 

app = Flask(__name__) 

loan_limits = 5 


def validate_loan_data(data): 
    required_fields = ['name', 'id', 'income', 'loan_amount'] 
    
    for field in required_fields: 
        if field not in data or not data[field]: 
            return False, f"{field} is required."
        
        
    if not data['id'].isdigit() or len(data['id']) != 10:
        return False, "ID must be 10 digits long."
    
    if not data['income'].isdigit() or int(data['income']) <= 0: 
        return False, "Loan amount must to be numeric." 
    
    income = int(data['income'])
    loan_amount = int(data['loan_amount'])
    if loan_amount > (loan_amount/100) * income: 
        return False, f"Loan amount connot exceed {loan_amount}% of income."
    
    return True, "Success!" 


@app.route('/')
def home():
    return  '''
    <!DOCTYPE html>
    <html leng="en">
    <head>
        <meta charset = "UTE-8">
        <meta name = "viewport" content= "width=device-width, inital-scale = 0.1">
        <title> Welcoming </title>
    </head>
    <body>
        <h1> Welcome, apply for your loan today!</h1> 
        <button onclick = "location.href = '/apply_loan_form';"> Apply for Loan </button>
    </body>
    </html>

'''

@app.route('/apply_loan_form') 
def apply_loan_form():
    return '''
    <!DOCTYPE html>
    <html leng="en">
    <head>
        <meta charset = "UTE-8">
        <meta name = "viewport" content= "width=device-width, inital-scale = 0.1">
        <title> Apply for Loan </title>
    </head>
    <body>
        <h1>Apply for your Loan</h1> 
        <form action="/apply_loan" method="POST">
            <lable for="name">Name:</lable><br>
            <input type = "text" id ="name" name ="name"><br><br>
            
            <lable for="id">ID (10 digits): </lable><br>
            <input type="text", id = "id" name= "id"><br><br>
            
            <lable for="income">Montly Income: </lable><br>
            <input type="text", id = "income" name= "income"><br><br>
            
            <lable for="loan_amount">Loan Amount:</lable><br>
            <input type="text", id = "loan_amount" name= "loan_amount"><br><br>
            
            <button type="submit">Submit</button>  
        </form>
    </body>
    </html>
'''

@app.route('/apply_loan', methods=['POST'])
def apply_loan():
    data = {
        "name" : request.form['name'], 
        "id" : request.form['id'], 
        "income" : request.form['income'], 
        "loan_amount" : request.form['loan_amount'], 
    }
    
    is_valid, message = validate_loan_data(data)
    
    if is_valid: 
        return jsonify({"status" : "success", "message" : "Loan application submitted successfully!"})
    
    else: 
        return jsonify({"status" : "error", "message": message}), 400 
    
    
if __name__ == "__main__": 
    app.run(debug = True) 