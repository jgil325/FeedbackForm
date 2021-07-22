from signup import RegistrationForm
from login import LoginForm
from survey import SurveyForm
import time
import random
import threading
try:
    from flask import Flask, render_template, url_for, flash, redirect, request
    from flask_sqlalchemy import SQLAlchemy
    from flask_login import LoginManager, UserMixin
    from flask_login import login_user, logout_user
    from flask_login import current_user, login_required
except ImportError:
    print("Import Error")
# this gets the name of the file so Flask knows it's name
app = Flask(__name__)
app.config['SECRET_KEY'] = '2d6ca153ea201fe4daf5a90f380026b5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class SurveyResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.String(2), nullable=False)
    comments = db.Column(db.String(524288), nullable=False)

    def __repr__(self):
        return f"SurveyResponse('{self.rating}', '{self.comments}')"

# Login Manager


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'Login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Admin Page


@app.route('/admin')
@login_required
def admin():
    name = current_user.username
    responses = db.execute("SELECT * FROM SurveyResponse")
    return render_template('admin.html', name=name, responses=responses)

# Logout


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('login'))

# Homepage


@app.route("/")
def layout():
    return render_template("home.html")

# SignUp


@app.route("/signup", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():  # checks if entries are valid
        username = request.form.get('username')
        email = request.form.get('email')
        user = User.query.filter_by(username=username).first()
        email_query = User.query.filter_by(email=email).first()
        if user and email_query:
            flash('username and email is already in use.')
            return redirect(url_for('register'))
        elif user:
            flash('username is already in use.')
            return redirect(url_for('register'))
        elif email_query:
            flash('email is already in use.')
            return redirect(url_for('register'))
        else:
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('login'))
    return render_template('signup.html', title='SignUp', form=form)

# Login


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        pwd = User.query.filter_by(password=password).first()
        if not user:
            flash('No user found. PLease Login or Sign up!')
            return redirect(url_for('login'))
        elif not pwd:
            flash('PLease check your login details and try again')
            return redirect(url_for('login'))
        flash('Login Success')
        login_user(user)
        return redirect(url_for('admin'))
    return render_template("login.html", form=form)

# API Page


@app.route("/api")
def api():
    return render_template("api.html", subtitle='API')

# About Page


@app.route("/about")
def about():
    return render_template("about.html", subtitle='About Page')

# Survey Page


@app.route("/survey", methods=['GET', 'POST'])
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        email = request.form.get('email')
        rating = request.form.get('rating')
        comments = request.form.get('comments')
        response = SurveyResponse(
                name=form.name.data,
                email=form.email.data,
                rating=form.rating.data,
                comments=form.text_area.data)
        db.session.add(response)
        db.session.commit()
        flash(f'Survey Submitted for {form.name.data}!', 'success')
    return render_template("survey.html", form=form)


# Main Function
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
