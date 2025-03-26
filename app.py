from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Index route
@app.route("/")
def index():
    return render_template("index.html")

# Login route
@app.route("/login")
def login():
    return render_template("login.html") 

# Signup route
@app.route("/signup")
def signup():
    return render_template("signup.html")  
    
# Self-help guide route
@app.route("/self_guide")
def self_guide():
    return render_template("self_guide.html")

@app.route("/games")
def games():
    return render_template("gamesindex.html")

@app.route("/musicplayer")
def music_player():
    return render_template("Playlist_English.html")

# About route
@app.route("/about")
def about():
    return render_template("about.html") 

if __name__ == '__main__':
    app.run(debug=True)