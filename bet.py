import sqlite3

def create_bet(cur, desc, answers):
    try:
        cur.execute("INSERT into paris ('result', 'total') (0, 0)")
    except sqlite3.Error as er:
        return "Je n'ai pas réussis à créer votre paris"
    return "Votre paris: " + desc + " réponse possible: 1 => " + answers[0] + ", 2 =>  " + answers[1]
