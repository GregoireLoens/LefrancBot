import sqlite3
from Gambler import gambler

class Bet():

    _table = "bets"

    def __init__(self, id=None):
        con = sqlite3.connect('../../db/franc.db')
        self._cursor = con.cursor()
        self.id = id
        self._exist = False
        self._gamblers = []
        try:
            self._cursor.execute("Select pot, open from ? where id = ?;", self._table, self._id)
            self._pot = self._cursor.fetchone()[0]
            self._exist = True
            self._open = self._cursor.fetchone[1]
            self._cursor.execute("Select id from gamblers where bet_id = ?;", id)
            for elem in self._cursor:
                self._gamblers.append(Gambler(elem[0]))
        except:
            self._cursor.execute("INSERT INTO paris ('result', 'total_amount', 'open') VALUES (0, 0, 1)")
            self._pot = 0
            self.lastrowid()
            self._open = True
            self._gamblers = []
    
    def close_bet(self):
        self._cursor.execute("UPDATE paris set open=0 where id= ?", self.id)
        self._open = False

    def is_open(self):
        self._open
    