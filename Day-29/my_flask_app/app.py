from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated user database
users = {
    'user1': {'password': 'password1', 'profile': {'username': 'user1', 'name': 'John Doe', 'email': 'john@example.com'}},
    'user2': {'password': 'password2', 'profile': {'username': 'user2', 'name': 'Jane Smith', 'email': 'jane@example.com'}}
}

@app.route('/')
def index():
    if 'username' in session:
        return redirect('/profile')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username]['password'] == password:
        session['username'] = username
        return redirect('/profile')
    return redirect('/')

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        profile = users[username]['profile']
        return render_template('profile.html', profile=profile)
    return redirect('/')

@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'username' in session:
        session_username = session['username']
        username = request.form['username']
        if session_username == username:
            name = request.form['name']
            email = request.form['email']
            users[username]['profile']['name'] = name
            users[username]['profile']['email'] = email
            return redirect('/profile')
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
