# Day-29 OWASP TOP 10: 1 BROKEN ACCESS CONTROL
## Flask Application with Broken Access Control

This Flask application demonstrates a broken access control vulnerability, where users can update each other's profiles due to improper session handling. Below, we explain the issue, provide the code snippets, and offer a graphical flowchart to illustrate the problem.

`  Please read the whole README file before doing anything. All instructions are provided in detailed manner. `
## Structure

```
my_flask_app/
├── templates/
│   ├── login.html
│   ├── profile.html
├── app.py
```

## Installation

1. **Clone the repository:**
   ```bash
    wget https://raw.githubusercontent.com/Heartking-2324/Cybersecurity-90days_notes/main/Day-29/my_flask_app
    cd my_flask_app
   ```

3. **Install dependencies:**
   ```bash
   pip install flask
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open a web browser and go to `http://127.0.0.1:5000/`.

### To check the code you can see from the [my_flask_app](https://github.com/Heartking-2324/Cybersecurity-90days_notes/tree/main/Day-29/my_flask_app)


## Broken Access Control Issue

The application has a vulnerability where users can update each other's profiles due to improper session handling in the `update_profile` route. 

### Graphical Explanation

```plaintext
[ Start ]
     |
     v
[ User1 Logs In ]
     |
     v
[ User1 Updates Profile ]
     |
     v
[ User2 Logs In ]
     |
     v
[ User2 Sees User1's Updated Profile ]
     |
     v
[ User2 Updates Profile ]
     |
     v
[ User1 Logs In Again ]
     |
     v
[ User1 Sees User2's Updated Profile ]
     |
     v
[ End ]
```

### Step-by-Step Explanation

1. **User1 Logs In:**
   - User1 enters username `user1` and password `password1`.
   - The session stores `username = user1`.

2. **User1 Updates Profile:**
   - User1 changes the name and email to `John Smith` and `johnsmith@example.com`.
   - The application does not properly verify that the user should only update their own profile.
   - The `update_profile` function mistakenly allows the update because the session username is not properly checked.

3. **User2 Logs In:**
   - User2 enters username `user2` and password `password2`.
   - The session stores `username = user2`.

4. **User2 Sees User1's Updated Profile:**
   - User2 sees `John Smith` and `johnsmith@example.com` instead of `Jane Smith` and `jane@example.com`.
   - This happens because the profile data is shared or overwritten due to improper access control.

5. **User2 Updates Profile:**
   - User2 changes the profile information.
   - The application again does not properly restrict the update.

6. **User1 Logs In Again:**
   - User1 now sees User2's updated profile instead of their own.

## Fixing the Broken Access Control

To fix the broken access control, ensure that users can only update their own profiles. Here's how to correctly implement this:

**Modify the `update_profile` Function:**

Ensure that the `username` in the session matches the `username` in the form before allowing updates.

```python
@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'username' in session:
        session_username = session['username']
        if session_username in users:
            name = request.form['name']
            email = request.form['email']
            users[session_username]['profile']['name'] = name
            users[session_username]['profile']['email'] = email
            return redirect('/profile')
    return redirect('/')
```

**Ensure the Form Hidden Field Matches Session Username:**

Remove the hidden `username` field from the profile update form.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Profile</title>
</head>
<body>
    <h2>Profile</h2>
    <form action="/update_profile" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{{ profile.name }}" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" value="{{ profile.email }}" required>
        <br>
        <button type="submit">Update</button>
    </form>
    <a href="/logout">Logout</a>
</body>
</html>
```

### Correct Workflow:

1. **Run the Flask Application:**
   ```bash
   python app.py
   ```
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-29/app_py.png?raw=true)
2. **Access the Application:**
   Open a web browser and go to `http://127.0.0.1:5000/`.

3. **Login:**
   - Username: `user1`
   - Password: `password1`
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-29/user1_show_change.jpg?raw=true)
4. **Update Profile:**
   - Change `Name` to `John Smith`.
   - Change `Email` to `johnsmith@example.com`.
   - Click "Update".
   - User1's profile should now show `John Smith` and `johnsmith@example.com`.
![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-29/user1_changed_made.png?raw=true)
5. **Login as User2:**
   - Username: `user2`
   - Password: `password2`
  ![](https://github.com/Heartking-2324/Cybersecurity-90days_notes/blob/main/Day-29/user2_show.jpg?raw=true)
