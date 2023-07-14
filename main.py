from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy

app = Flask(__name__)
proxied = FlaskBehindProxy(app) 
app.config['SECRET_KEY'] = 'f46d9cffd6774fefbe29c89f0ed3dc39'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='', text='Please Select Login Portal Above.')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    return render_template('recommend.html')

@app.route('/proxy/5000/index')
def index():
    return render_template('index.html')
# @app.route("/doctor_login")
# def doct():
#     return render_template('doctor.html', subtitle='Doctor Sign In Page', text='Please Log In.')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Log In', form=form)


# @app.route("/patient_login", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit(): # checks if entries are valid
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home')) # if so - send to home page
#     return render_template('register.html', title='Log In', form=form)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
