import sqlite3

def create_bet(cur, desc, answers):
    try:
        cur.execute("INSERT INTO paris ('result', 'total', 'ouvert') VALUES (0, 0, 1)")
    except sqlite3.Error as er:
        return "Je n'ai pas réussis à créer votre paris"
    
    return "Votre paris: '" + desc + "' est validé,\nles réponses possibles: 1 => " + answers[0] + ", 2 =>  " + answers[1] + "\nPour parier utilisez l'id: " + str(cur.lastrowid)

def close_bet(cur, id):
    try:
        cur.execute("update paris set ouvert=0 where id=" + id)
    except sqlite3.Error as er:
        return "Je n'ai pas réussis à fermer votre"
    return "le paris numéro: " + str(cur.lastrowid) + " est fermé" 