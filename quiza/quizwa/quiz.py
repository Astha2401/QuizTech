from flask import Flask, render_template, request, redirect, url_for, session

import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL database connection details
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'quizwa',
    'raise_on_warnings': True
}

# Function to get a database connection
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Signup route
@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Insert user data into the 'users' table
        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(insert_query, (username, password))
            connection.commit()

            cursor.close()
            connection.close()

            return redirect(url_for('login'))
        except Exception as e:
            return f'Error: {str(e)}'

    return render_template('signup.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Check user credentials in the 'users' table
        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            select_query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(select_query, (username, password))
            user = cursor.fetchone()

            if user:
                # Set the user session
                session['username'] = user[1]
                return redirect(url_for('categories'))
            else:
                error = 'Invalid credentials. Please try again.'
                return render_template('login.html', error=error)

            cursor.close()
            connection.close()

        except Exception as e:
            return f'Error: {str(e)}'

    return render_template('login.html')

# Categories page route
@app.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'POST':
        category_id = request.form['category_id']
        return redirect(url_for('quiz', category_id=category_id))

    # Retrieve the available quiz categories from the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    conn.close()
    return render_template('categories.html', categories=categories)

# Quiz page route
@app.route('/quiz/<int:category_id>', methods=['GET', 'POST'])
def quiz(category_id):
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Process the form submission
        selected_options = []
        for key, value in request.form.items():
            if key.startswith('question_'):
                question_id = int(key.split('_')[1])
                option_id = int(value)
                selected_options.append({'question_id': question_id, 'option_id': option_id})
        
        # Store the user's selected options in session
        session['selected_options'] = selected_options

        return redirect(url_for('result'))
    else:
        # Display the quiz form
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if the category exists in the database
        cursor.execute('SELECT * FROM categories WHERE id = %s', (category_id,))
        category = cursor.fetchone()
        if not category:
            error = 'Category not found'
            return render_template('error.html', error=error)

        # Retrieve the quiz questions and options for the selected category from the database
        cursor.execute('SELECT * FROM questions WHERE category_id = %s', (category_id,))
        questions = cursor.fetchall()

        for question in questions:
            cursor.execute('SELECT * FROM options WHERE question_id = %s', (question[0],))
            options = cursor.fetchall()
            question['options'] = options

        conn.close()

        return render_template('quiz.html', questions=questions)



# Result page route
@app.route('/result', methods=['POST'])
def result():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    # Retrieve the user's selected options from session
    selected_options = session.get('selected_options')
    if not selected_options:
        return redirect(url_for('categories'))  # Redirect the user if selected options are not found

    # Retrieve the user's information (e.g., name, email) from the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user = cursor.fetchone()
    conn.close()

    return render_template('result.html', user=user, selected_options=selected_options)


# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
