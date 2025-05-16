from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

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
        data = {
            'full_name': request.form['full_name'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'cnic': request.form['cnic'],
            'people': request.form['people'],
            'date': request.form['date'],
            'timing': request.form['timing'],
            'message': request.form['message']
        }
        with open('bookings.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data.values())
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
