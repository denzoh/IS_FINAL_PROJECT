from flask import Flask, render_template


app = Flask(__name__)


@app.route('/login')
def login():
    return render_template("login.html");

@app.route('/register')
def sign_up():
    return render_template("register.html");

@app.route('/tweets')
def tweet():
    return render_template("tweet.html");

@app.route('/search')
def search():
    return render_template("search.html");



if __name__ == '__main__':
    app.run()
