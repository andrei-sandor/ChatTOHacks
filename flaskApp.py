from flask import Flask, render_template
from ChatMojiBot import *


app = Flask(__name__)

@app.route('/')
def sessions():
    return render_template('index.html')


async def textToEmoji(methods = ['GET']):
    await send_receive()
