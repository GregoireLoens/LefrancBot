import sqlite3

def create_bet(cur, desc, answers):
    try:
        cur.execute("INSERT INTO paris ('result', 'total', 'ouvert') VALUES (0, 0, 1)")
    except sqlite3.Error as er:
        return "Je n'ai pas réussis à créer votre paris"
    
    return "Votre paris: '" + desc + "' est validé,\nles réponses possibles: 1 => " + answers[0] + ", 2 =>  " + answers[1] + "\nPour parier utilisez l'id: " + str(cur.lastrowid)

def close_bet(cur, id):
    try:
        cur.execute("UPDATE paris set ouvert=0 where id=" + id)
    except sqlite3.Error as er:
        return "Je n'ai pas réussis à fermer votre paris"
    return "le paris numéro: " + str(cur.lastrowid) + " est fermé" 

def is_open(cur, id):
    try:
        cur.execute("SELECT ouvert from paris where id=" + id + ";")
    except sqlite3.Error as er:
        return -1
    is_open = cur.fetchone()
    return is_open[0]

def bet(cur, id, choice, amount):
    if is_open(cur, id) == 1:
        try:
            cur.execute("INSERT INTO parieurs ('choix', 'somme', 'id_paris') VALUES (" +  choice + "," + amount + "," + id + ");")
        except sqlite3.Error as er:
            return "Je n'ai pas réussis à prendre en compte votre paris"
        return "Vous avez parié " + amount + " francs sur le paris numéro " + id
    else: 
        return "Vous ne pouvez plus miser sur ce paris"