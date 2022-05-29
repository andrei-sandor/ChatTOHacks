from flask import Flask, render_template
from ChatMojiBot import *


app = Flask(__name__)

@app.route('/')
def sessions():
<<<<<<< Updated upstream
    return render_template('ui.html')
=======
    return render_template('index.html')
>>>>>>> Stashed changes

async def textToEmoji(methods = ['GET']):
    await send_receive()
