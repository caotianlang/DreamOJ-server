import sqlite3

class Database:
    def __init__(self, dbname):
        self.dbname = dbname

    def createUserTable(self):
        with sqlite3.connect(self.dbname) as database:
            createTableCmd = '''create table if not exists user(id integer PRIMARY KEY autoincrement, username TEXT, password TEXT)'''
            database.execute(createTableCmd)
    
    def query(self, name):
        with sqlite3.connect(self.dbname) as database:
            queryCmd = '''select * from user where username = :name'''
            result = database.execute(queryCmd, {'name':name})
            return result.fetchall()

    def insert(self, name, password):
        with sqlite3.connect(self.dbname) as database:
            insertCmd = '''
            insert into user
            (id, username, password)
            values
            (NULL, :name, :pwd)
            '''
            database.execute(insertCmd, {'name':name, 'pwd':password})
            database.commit()