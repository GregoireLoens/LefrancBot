import sqlite3

def connect_db():
    con = sqlite3.connect('../../db/franc.db')
    cur = con.cursor()
    return cur

def get_salaries(cur):
    cur.execute("SELECT c.discord_id, c.date_paye, r.salary FROM comptes c INNER JOIN roles r on c.role_id = r.discord_role_id")
    res = cur.fetchall()
    return res

def update_month(cur, discord_id, month):
    param = (month, discord_id)
    cur.execute("UPDATE comptes SET date_paye = ? WHERE discord_id = ?", param)

def check_account(cur, message):
    cur.execute("SELECT francs FROM comptes WHERE pseudo = ?", message.author.name)
    res = cur.fetchone()
    str = 'Your account value is ' + res[0]
    return str

def register_roles(cur, message, val):
    cur.execute("INSERT INTO roles (salary, discord_role_id) VALUES ?", val)

def register_members(cur, message):
    return ('Not yet implemented')

def add_points(cur, discord_id, points):
    cur.execute("SELECT francs FROM comptes WHERE discord_id = ?", discord_id)
    res = cur.fetchone()
    val = res[0]
    val += points
    param = (val, discord_id)
    cur.execute("UPDATE comptes SET francs = ? WHERE discord_id =?", param)

def decrease_points(cur, discord_id, points):
    cur.execute("SELECT francs FROM comptes WHERE discord_id = ?", discord_id)
    res = cur.fetchone()
    val = res[0]
    val -= points
    param = (val, discord_id)
    cur.execute("UPDATE comptes SET francs = ? WHERE discord_id =?", param)
