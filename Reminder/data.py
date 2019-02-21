import sqlite3
import os.path

class Database():
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.base = self.connection.cursor()
        self.__isempty()

    def __create_table(self):
        self.base.execute('''CREATE TABLE reminders
                            (title text, price real, date text, tag text, description text)''')

    def __isempty(self):
        try:
            self.base.execute('SELECT * FROM reminders')
        except:
            self.__create_table()
            print('new table')

    def add(self, data_tuple):
        self.base.execute('INSERT INTO reminders VALUES (?, ?, ?, ?, ?)', data_tuple)

    def pull(self, title):
        search = (title,)
        self.base.execute('SELECT * FROM reminders WHERE title=?', search)
        return self.base.fetchone()

    def pull_all(self):
        self.base.execute('SELECT * FROM reminders')
        return self.base.fetchall()

    def delete(self, title):
        search = (title,)
        self.base.execute('DELETE FROM reminders WHERE title=?', search)

    def close(self):
        self.connection.commit()
        self.connection.close()
