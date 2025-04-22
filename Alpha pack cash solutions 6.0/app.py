from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Dummy user data (replace with database logic)
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
        
        # Add your password validation logic here
        if password == confirmPassword:
            hashed_password = generate_password_hash(password)
            users.append({'name': name, 'email': email, 'phone': phone, 'password': hashed_password})
            return redirect(url_for('login'))
        else:
            return 'Passwords do not match', 400

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Check user in the list (replace with actual DB query)
        user = next((u for u in users if u['email'] == email), None)
        
        if user and check_password_hash(user['password'], password):
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials', 401
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return 'Welcome to your Dashboard'

if __name__ == '__main__':
    app.run(debug=True)
