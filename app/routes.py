from app import app
from flask import render_template

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Disclaimer page route
@app.route('/disclaimer/')
def disclaimer():
    return render_template('disclaimer.html')

# Homepage route
@app.route('/homepage/')
def homepage():
    return render_template('homepage.html')

# Links page route
@app.route('/links/')
def links():
    return render_template('links.html')

# Login page route
@app.route('/login/')
def login():
    return render_template('login.html')

# Server List page route
@app.route('/server-list/')
def server_list():
    return render_template('server_list.html')
