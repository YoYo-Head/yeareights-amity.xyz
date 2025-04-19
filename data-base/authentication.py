from flask import Flask, render_template, request, send_file
import socket as clct
import time

app = Flask(__name__)

checker = True
myIP = '203.221.138.117'

t = time.localtime()

# How often should the program check for IP (put 62 for only once every minute )
oftenCheck = 5

@app.route('/')
def indexHTML():
    return render_template('index.html')

@app.route('authenticating/')
def authenticate():

    time.wait(3)

    secs = str(t.tm_sec)
    checkTime = (int(secs) % oftenCheck) -1

    hostName = clct.gethostname()
    IPadrs = clct.gethostbyname(hostName)

    if checkTime == 0 or secs == 1:
        if IPadrs == myIP:
            print("redirecting to data base")
            return render_template('info/')

        else:
            print("You are not authorised to access!")
            return render_template('denied/')

if __name__ == '__main__':
    app.run(debug=False)