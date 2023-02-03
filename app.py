from flask import *
from flask_cors import *
import sqlite3

assetPath = './assets'
dbname = 'Database.db'

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
    def createUserTable(self):
        with sqlite3.connect(dbname) as database:
            try:
                createTableCmd = '''
                create table if not exist user(
                    id integer PRIMARY KEY autoincrement,
                    username Text,
                    password Text,
                )
                '''
                database.execute(createTableCmd)
                database.commit()
            except:
                print('Cannot create user table.')
    
    def query(self, name):
        with sqlite3.connect(dbname) as database:
            try:
                queryCmd = '''
                select * from user where username = :name    
                '''
                result = database.execute(queryCmd, {'name':name})
                database.commit()
                return result
            except:
                print('Cannot query.')

    def insert(self, name, password):
        with sqlite3.connect(dbname) as database:
            try:
                insertCmd = '''
                insert into user
                (id, username, password)
                values
                (NULL, :name, :pwd)
                '''
                database.execute(insertCmd, {'name':name, 'pwd':password})
                database.commit()
            except:
                print('Cannot insert.')

if __name__ == '__main__':
    db = Database()
    db.createUserTable()
    db.insert('testuser', 'cccccc')

    print ('hello')

    app.run()