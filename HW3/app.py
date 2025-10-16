from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/profile', methods=['POST'])
def profile():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    gender = request.form['gender']
    status = request.form['status']
    location = request.form['location']
    
    return render_template('profile.html',
                           firstname=firstname,
                           lastname=lastname,
                           gender=gender,
                           status=status,
                           location=location)

if __name__ == '__main__':
    app.run(debug=True)
