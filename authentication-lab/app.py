from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase 

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
const firebaseConfig = {

  "apiKey": "AIzaSyArWxllAd3iJglgNz_RYQK-z1nSzmepIDY",

  "authDomain": "intrepid-fiber-328519.firebaseapp.com",

  "projectId": "intrepid-fiber-328519",

  "storageBucket": "intrepid-fiber-328519.appspot.com",

  "messagingSenderId": "978423849068",

  "appId": "1:978423849068:web:3eada0ef0c19cf86763849",

  "measurementId": "G-M1SX87MV99"

  "databaseURL": "https://intrepid-fiber-328519-default-rtdb.firebaseio.com/"
};

firebace = pyrebase.initializeApp(firebaseConfig)
analytics = firebace.auth()
db = firebase.databse()

@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method = "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            login_session["logged_user"] = analytics.sign_in_with_email_and_password(email, password)
            return redirect(url_for("/add_tweet"))
        except:
            error = "login failed"
    else:
        return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method = "POST":
        email = request.form["email"]
        password = request.form["password"]
        username = request.form["username"]
        name = request.form["name"]
        bio = request.form["bio"]

        try:
            login_session["user"] = analytics.create_user_with_email_and_password(email, password)
            user = {
                "email": email,
                "password": password,
                "username": username,
                "name": name,
                "bio": bio
            }
            UID = login_session["user"]["localId"]
            append_user = db.child("users").child(UID).set(user)
            return redirect(url_for("/add_tweet"))
        except:
            error = "authorize failed"
    else:
        return render_template("signup.html")

@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    error = ""
    if request.method = "POST"
        UID = login_session["logged_user"]["localId"]
        title = request.form["title"]
        text = request.form["text"]

        tweet = {UID: {"title": title, "text": text}}
        
        db.child("Tweets").push(tweet)

        return render_template("add_tweet.html", db.child("Tweets").get().val())
    else:
        return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)