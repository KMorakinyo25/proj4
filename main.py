from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
proxied = FlaskBehindProxy(app) 
app.config['SECRET_KEY'] = 'f46d9cffd6774fefbe29c89f0ed3dc39'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)
  select = db.Column(db.String(2), nullable= False)


  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

with app.app_context():
  db.create_all()


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

@app.route("/patient")
def pat():
    return render_template('patient.html', subtitle='Patient Page', text='Welcome')

@app.route("/symptoms")
def symp():
    return render_template('symptoms.html', subtitle='Symptoms', text='Please List Your Symptoms')

@app.route("/doctor")
def doct():
    return render_template('doctors.html', subtitle='Doctor Page', text='Welcome')



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        user = User(username=form.username.data, email=form.email.data, password=form.password.data, select=form.select.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        if user.select == 'pt':
          return redirect(url_for('pat'))
        else:
          return redirect(url_for('doct'))
    return render_template('register.html', title='Log In', form=form)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
