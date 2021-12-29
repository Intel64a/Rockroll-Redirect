from flask import Flask
from flask import render_template
import playsound

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rockroll')
def rockroll():
    playsound.playsound("rockroll.wav")

if(__name__ == "__main__"):
    app.run(port='8080', debug=True)