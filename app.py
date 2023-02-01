from flask import *
from flask_cors import *

assetPath = './assets'

app = Flask(__name__)
CORS(app, supports_credentials = True)

@app.route('/')
def main():
    return '<h1>This is DreamOJ-sever</h1>'

@app.route('/images/<filename>')
def sendImage(filename):
    return send_file(assetPath + '/images/' + filename)

@app.route('/login', methods = ['POST'])
def login():
    return jsonify({'ok' :'ok'})

class Database:
    def __init__():
        pass
    

if __name__ == '__main__':
    app.run()