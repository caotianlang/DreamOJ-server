from flask import *
from flask_cors import *
from database_util import *

assetPath = './assets'
dbname = 'Database.db'
db = Database(dbname)

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
    data = request.get_json()

    q = db.query(data['username'])
    
    if  len(q) == 0:
        return jsonify({'login':'username'}) 
    else :
        for row in q:
            if row[2] == data['password']:
                return jsonify({'login':'ok'})
        print (data['password'])
        return jsonify({'login':'password'})

@app.route('/signup', methods = ['POST'])
def signup():
    data = request.get_json()
    if db.query(data['username']):
        return jsonify({'signup' : 'username'})
    
    db.insert(data['username'], data['password'])
    return jsonify({'signup' : 'ok'})

if __name__ == '__main__':
    db.createUserTable()

    app.run()