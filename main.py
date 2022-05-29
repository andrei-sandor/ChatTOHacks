from flask import Flask, render_template
from ChatMojiBot import *


app = Flask(__name__)

@app.route('/')
def sessions():
    return render_template('index.html')


async def textToEmoji(methods = ['GET']):
    await send_receive()

    @app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
