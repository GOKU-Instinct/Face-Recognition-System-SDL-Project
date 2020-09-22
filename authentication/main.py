from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/profile')
def success():
    return render_template('profile.html')

@app.route('/new')
def newuser():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug = True)