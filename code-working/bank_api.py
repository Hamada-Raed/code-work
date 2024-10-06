from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/welcome/<name>')
def welcome(name):
    return f"Welcome {name}!"

@app.route('/')
def home():
    return 'Flask is running!'

@app.route('/Loans', methods=['PUT'])
def updateLoans():
    new_loan_id = request.args.get('new_loan_id')
    new_customer_id = request.args.get('new_customer_id')
    new_loan_amount = request.args.get('new_loan_amount')
    new_interest_rate = request.args.get('new_interest_rate')
    new_loan_status = request.args.get('new_loan_status')
    new_start_date = request.args.get('new_start_date')
    new_end_date = request.args.get('new_end_date')

    loan_id = request.args.get('loan_id')
    customer_id = request.args.get('customer_id')
    loan_amount = request.args.get('loan_amount')
    interest_rate = request.args.get('interest_rate')
    loan_status = request.args.get('loan_status')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    newValues = {}
    if new_loan_id:
        newValues["loan_id"] = new_loan_id
    if new_customer_id:
        newValues["customer_id"] = new_customer_id
    if new_loan_amount:
        newValues["loan_amount"] = new_loan_amount
    if new_interest_rate:
        newValues["interest_rate"] = new_interest_rate
    if new_loan_status:
        newValues["loan_status"] = new_loan_status
    if new_start_date:
        newValues["start_date"] = new_start_date
    if new_end_date:
        newValues["end_date"] = new_end_date

    filter = {}
    if loan_id:
        filter["loan_id"] = loan_id
    if customer_id:
        filter["customer_id"] = customer_id
    if loan_amount:
        filter["loan_amount"] = loan_amount
    if interest_rate:
        filter["interest_rate"] = interest_rate
    if loan_status:
        filter["loan_status"] = loan_status
    if start_date:
        filter["start_date"] = start_date
    if end_date:
        filter["end_date"] = end_date

    query = "UPDATE Loans"
    if newValues:
        query += " SET "
        for key, value in newValues.items():
            query += f"{key} = '{value}', "
        query = query[:-2]  
    else:
        return jsonify({"message": "Nothing to change"})

    if filter:
        query += " WHERE "
        for key, value in filter.items():
            query += f"{key} = '{value}' AND "
        query = query[:-5] 

    conn = sqlite3.connect('BankDB.db')
    cursor = conn.cursor()
    isSuccessful = True
    try:
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(f"Error: {e}") 
        isSuccessful = False
    finally:
        conn.close()

    return jsonify({"success": isSuccessful})

if __name__ == '__main__':
    app.run(debug=True)
