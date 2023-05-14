from flask import Flask
from flask import request
from requests.system import *
from requests.level import *
from requests.crossword import *
from requests.wordSound import *

app = Flask(__name__)

@app.route('/<name>')
def dashboard(name):
   return f"welcome {name}"

@app.route('/check')
def checkConnectRequest():
   return System(app).checkConnect(request)

@app.route('/appInit')
def appInitRequest():
    return System(app).appInit(request)

@app.route('/getLevel')
def getLevelRequest():
    return Level(app).getLevel(request)

@app.route('/getLevels')
def getLevelsRequest():
    return Level(app).getLevels(request)

@app.route('/crosswords')
def crosswordsRequest():
    return Crosswords(app).crosswords(request)

@app.route('/wordSound')
def wordSoundRequest():
    return WordSound(app).wordSound(request)

if __name__ == '__main__':
    # app.run(host='82.146.49.164', port=8005, debug = True)
    app.run(host='localhost', port=8005, debug = True)
