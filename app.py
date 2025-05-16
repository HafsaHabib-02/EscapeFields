from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Flask app
app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/facilities')
def facilities():
    return render_template('facilities.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/book_now', methods=['GET', 'POST'])
def book_now():
    if request.method == 'POST':
        data = (
            request.form['full_name'],
            request.form['phone'],
            request.form['email'],
            request.form['cnic'],
            int(request.form['people']),
            request.form['date'],
            request.form['timing'],
            request.form['message']
        )
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO bookings (full_name, phone, email, cnic, people, date, timing, message)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('thankyou'))
    return render_template('book_now.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
