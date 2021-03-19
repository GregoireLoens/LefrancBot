import sqlite3

def connect_db():
    con = sqlite3.connect('../../db/franc.db')
    cur = con.cursor()
    return cur

def add_points(cur, pseudo, points):
    param = (pseudo,)
    cur.execute("SELECT francs FROM comptes WHERE pseudo = ?", param)
    res = cur.fetchone()
    val = res[0]
    val += points
    cur.execute("UPDATE comptes SET francs = ? WHERE pseudo =?", param)

def decrease_points(cur, pseudo, points):
    cur.execute("SELECT francs FROM comptes WHERE pseudo = ?", pseudo)
    res = cur.fetchone()
    val = res[0]
    val -= points
    param = (val, pseudo)
    cur.execute("UPDATE comptes SET francs = ? WHERE pseudo =?", param)