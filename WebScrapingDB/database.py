import sqlite3

def create_table(dbname):
    print("Connecting to the database {}...".format(dbname))
    conn = sqlite3.connect(dbname)
    print("Connected to database {} successfully!".format(dbname))
    
    cur = conn.cursor()
    cur.execute(" CREATE TABLE IF NOT EXISTS HOTELS (NAME TEXT, ADDRESS VARCHAR(200), PRICE INTEGER, RATING FLOAT, AMENITIES VARCHAR(200)) ")

    conn.close()

def insert_into_table(dbname, values):
    print("Connecting to the database {}...".format(dbname))
    conn = sqlite3.connect(dbname)
    print("Connected to database {} successfully!".format(dbname))

    cur = conn.cursor()
    cur.execute(" INSERT INTO HOTELS (NAME, ADDRESS, PRICE, RATING, AMENITIES) VALUES (?, ?, ?, ?, ?) ", values)
    conn.commit()
    print("Inserted a row into the table: {}".format(values))

    conn.close()

def get_table_data(dbname):
    print("Connecting to the database {}...".format(dbname))
    conn = sqlite3.connect(dbname)
    print("Connected to database {} successfully!".format(dbname))

    cur = conn.cursor()
    cur.execute(" SELECT * FROM HOTELS ")
    table_data = cur.fetchall()

    #to find the count of the total rows use len(table_data)
    for record in table_data:
        print(record)

    conn.close()