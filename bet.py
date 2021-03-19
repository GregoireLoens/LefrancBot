import sqlite3

def create_bet(cur, desc, answers):
    try:
        cur.execute("INSERT INTO paris ('result', 'total') VALUES (0, 0)")
    except sqlite3.Error as er:
        return "Je n'ai pas réussis à créer votre paris"
    
    return "Votre paris: '" + desc + "' est validé,\nles réponses possibles: 1 => " + answers[0] + ", 2 =>  " + answers[1] + "\nPour parier utilisez l'id: " + str(cur.lastrowid)
