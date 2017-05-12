from flask import Flask, render_template, redirect, request, session, flash
import re, datetime

app=Flask(__name__)
app.secret_key = 'whaaaaat'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d\W]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    valid = True
    #first/last name
    if len(request.form['fname']) < 1:
        flash("First name field is required")
        valid = False
    elif not request.form['fname'].isalpha():
        flash("The first name you entered is not valid")
        valid = False

    if len(request.form['lname']) < 1:
        flash("Last name field is required")
        valid = False
    if not request.form['lname'].isalpha():
        flash("The last name you entered is not valid")
        valid = False

    #email
    if len(request.form['email']) < 1:
        flash("Email field is required")
        valid = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("The email you entered is not valid")
        valid = False

    #birthdate
    try:
        bday = request.form['birthdate'].split('/')
        bday = datetime.date(int(bday[2]),int(bday[0]),int(bday[1]))
        if bday > datetime.date.today():
            flash("You haven't been born yet!")
            valid = False
    except:
        flash("The birthdate you entered is invalid")
        valid = False


    #passwords
    if request.form['password'] != request.form['cpassword']:
        flash("Passwords do not match")
        valid = False
    if not PW_REGEX.match(request.form['password']):
        flash("The password must include at least 1 number and 1 capital letter")

    if valid: flash("Thanks for submitting your information.")

    return redirect('/')

app.run(debug=True)
