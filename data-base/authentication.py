from flask import Flask, render_template, request
import socket as clct
import time

app = Flask(__name__)

checker = True
myIP = '203.221.138.117'

t = time.localtime()

# How often should the program check for IP (put 62 for only once every minute )
oftenCheck = 5

@app.route('/')
def authenticate():

    time.wait(1)

    render_template('transfer/')

    secs = str(t.tm_sec)
    checkTime = (int(secs) % oftenCheck) -1

    hostName = clct.gethostname()
    IPadrs = clct.gethostbyname(hostName)

    if checkTime == 0 or secs == 1:
        if IPadrs == myIP:
            print("redirecting to data base")

        else:
            print("You are not authorised to access!")
            return render_template('denied/')

if __name__ == '__main__':
    app.run(debug=False)