from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase 

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
const firebaseConfig = {

  apiKey: "AIzaSyArWxllAd3iJglgNz_RYQK-z1nSzmepIDY",

  authDomain: "intrepid-fiber-328519.firebaseapp.com",

  projectId: "intrepid-fiber-328519",

  storageBucket: "intrepid-fiber-328519.appspot.com",

  messagingSenderId: "978423849068",

  appId: "1:978423849068:web:3eada0ef0c19cf86763849",

  measurementId: "G-M1SX87MV99"

};

const app = pyrebase.initializeApp(firebaseConfig);
const analytics = pyrebase.getAnalytics(app);


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method = "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            login_session["loged_user"] = [email, password]
            return redirect(url_for("/add_tweet"))
        except:
            return "login failed"
    else:
        return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method = "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            login_session["user"] = [email, password]
            return redirect(url_for("/add_tweet"))
        except:
            return "authorize failed"
    else:
        return render_template("signup.html")

@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)