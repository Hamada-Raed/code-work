from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configure the database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banking_system.db'
app.config['JWT_SECRET_KEY'] = "8f4e585bcd364f0c9d6eb5dff67f5a4ea780bb77dd75de6042c835d9600fd1bf"  
db = SQLAlchemy(app)
jwt = JWTManager(app)

# User model
class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(200))
    account_balance = db.Column(db.Float, default=0.0)

# Transaction model
class Transaction(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# Welcome route
@app.route("/")
def welcome():
    return '''
        <h1>WELCOME</h1>
    '''

# Registration route
@app.route('/register', methods=["POST"])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(name=data['name'], email=data['email'], password_hash=hashed_password, address=data['address'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': "User registered successfully!"}), 201 

# Login route
@app.route('/login', methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first() 
    if user and check_password_hash(user.password_hash, data['password']): 
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}) 
    return jsonify({'message': 'Invalid credentials!'}), 401

# Deposit route
@app.route('/deposit', methods=["POST"])
@jwt_required()
def deposit():
    user_id = get_jwt_identity()
    data = request.json 
    amount = data['amount']
    user = User.query.get(user_id) 
    user.account_balance += amount 
    db.session.commit()
    return jsonify({'message': "Deposit successful!", "new_balance": user.account_balance})

# Withdraw route
@app.route('/withdraw', methods=["POST"])
@jwt_required()
def withdraw():
    user_id = get_jwt_identity()
    data = request.json 
    amount = data['amount']
    user = User.query.get(user_id) 
    if user.account_balance >= amount:
        user.account_balance -= amount 
        db.session.commit()
        return jsonify({'message': "Withdraw successful!", "new_balance": user.account_balance})
    return jsonify({"message": "Insufficient funds"}), 400 

# Get transactions route
@app.route('/transactions', methods=["POST"])
@jwt_required()
def get_transactions():
    user_id = get_jwt_identity()
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': tx.id, 'type': tx.transaction_type, 'amount': tx.amount, "timestamp": tx.timestamp} for tx in transactions])

if __name__ == "__main__": 
    with app.app_context():
        db.create_all()  
    app.run(debug=True, port=5000)
