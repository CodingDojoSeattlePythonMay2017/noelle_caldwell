from flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)
app.secret_key = "secretsecretsecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    valid = True;
    if len(request.form['name']) < 1:
        flash("Name cannot be blank")
        valid = False
    elif not request.form['name'].isalpha():
        flash("Invalid name input")
        valid = False

    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank")
        valid = False
    elif len(request.form['comment']) > 120:
        flash("Comment cannot exceed 120 characters")
        valid = False

    #is there a way to keep the valid fields in the form?
    #a more efficient way than a valid variable to keep track?
    #can I format my html to display my validations next to the fields instead of all at the top?
    if valid:
        n = request.form['name']
        l = request.form['location']
        lang = request.form['language']
        c = request.form['comment']
        return render_template('result.html', name=n, location=l, language=lang, comment=c)
    else:
        return redirect('/')

app.run(debug=True)
