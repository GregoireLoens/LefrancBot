import sqlite3

def connect_db():
    con = sqlite3.connect('../../db/franc.db')
    cur = con.cursor()
    return cur

def give_points(cur, message):
    return ('Not Yet implemented')

def check_account(cur, message):
    cur.execute("SELECT francs FROM comptes WHERE pseudo = ?", message.author.name)
    res = cur.fetchone()
    str = 'Your account value is ' + res[0]
    return str

def register_members(cur, message):
    return ('Not yet implemented')

def add_points(cur, pseudo, points):
    cur.execute("SELECT francs FROM comptes WHERE pseudo = ?", pseudo)
    res = cur.fetchone()
    val = res[0]
    val += points
    param = (val, pseudo)
    cur.execute("UPDATE comptes SET francs = ? WHERE pseudo =?", param)

def decrease_points(cur, pseudo, points):
    cur.execute("SELECT francs FROM comptes WHERE pseudo = ?", pseudo)
    res = cur.fetchone()
    val = res[0]
    val -= points
    param = (val, pseudo)
    cur.execute("UPDATE comptes SET francs = ? WHERE pseudo =?", param)
