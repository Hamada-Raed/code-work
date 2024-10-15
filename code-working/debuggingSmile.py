from flask import Flask, jsonify,request
from flask_cors import CORS
import sqlite3

app =Flask(__name__)
CORS(app)





@app.route('/customers',methods=['GET'])
def getCustomerProfile  () :
      customerId=request.args.get('customer_id')
      first_name=request.args.get('first_name')
      date_of_birth=request.args.get('date_of_birth')
      address=request.args.get('address')
      phone=request.args.get('phone')
      email=request.args.get('email')
      account_type=request.args.get('account_type')
      conn = sqlite3.connect('BankDB.db')
      filter={}
      if customerId:
         filter["customer_id"]=customerId
      if first_name:
         filter["first_name"]=first_name
      if date_of_birth:
         filter["date_of_birth"]=date_of_birth
      if address:
         filter["address"]=address
      if phone:
         filter["phone"]=phone
      if email:
         filter["email"]=email
      if account_type:
         filter["account_type"]=account_type

      str="SELECT * FROM customers"

      if filter:
        str+=" WHERE "
        for key, value in filter.items():
            str+=f"{key} = '{value}' AND "
        str=str[:-5]  
     

      cursor = conn.cursor()
      cursor.execute(str)
      customer = cursor.fetchall()
      if customer:
        return jsonify(customer)
      else:
        return jsonify({"message": "Customer not found"})


if __name__  == '__main__':


    app.run(debug=True)