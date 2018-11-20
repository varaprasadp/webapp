import sqlite3

def connect():
    conn = sqlite3.connect('database.db')
    print ("Opened database successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS database (name TEXT, age INTEGER, gender TEXT)')
    print ("Table created successfully")
    conn.close()

