import sqlite3 as sql


def listExtension():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM GamePages WHERE popular = 'y'").fetchall()
    con.close()
    return data


def listGames():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM GamePages").fetchall()
    con.close()
    return data


def listCategories():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT category FROM GamePages").fetchall()
    con.close()
    return data
