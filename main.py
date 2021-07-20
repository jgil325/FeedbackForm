from flask import Flask, render_template, url_for, flash, redirect, request

# this gets the name of the file so Flask knows it's name
app = Flask(__name__)
app.config['SECRET_KEY'] = '2d6ca153ea201fe4daf5a90f380026b5'


# Homepage
@app.route("/")
def home():
    return render_template("home.html", subtitle='Home Page')

# API Page
@app.route("/api")
def api():
    return render_template("api.html", subtitle='API')

# Main Function
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
