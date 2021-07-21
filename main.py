from signup import RegistrationForm
import time
import random
import threading
try:
    from flask import Flask, render_template, url_for, flash, redirect
    from flask_sqlalchemy import SQLAlchemy
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

# Homepage


@app.route("/")
def layout():
    return render_template("home.html")

# SignUp


@app.route("/signup", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():  # checks if entries are valid
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home', id="/")) # if so - send to home page
    return render_template('signup.html', title='SignUp', form=form)

# Login


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")

# API Page
@app.route("/api")
def api():
    return render_template("api.html", subtitle='API')


@app.route("/about")
def about():
    return render_template("about.html", subtitle='About Page')


# Main Function
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
