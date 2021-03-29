import sqlite3
from threading import Lock
from toolkit.db import prevent_concurrent
from models.Model import Model
from models.Gambler import Gambler


# Lock used to prevent conccurent acces to the same table into the database
_bets_mutex = Lock()

class Bet(Model):

    _table = "bets"

    @prevent_concurrent(_bets_mutex)
    def __init__(self, id=0):
        super().__init__(id)
        self._exist = False
        try:
            cur = self._connection.cursor().execute("SELECT pot, open, result FROM bets WHERE id=?;", str(self._id))
            self._pot, self._open, self._result = cur.fetchone()
        except:
            self._connection.cursor().execute("INSERT INTO bets (pot, result, open) VALUES (0, 0, 1)")
            self._pot = 0
            self._id = self._connection.cursor().lastrowid
            self._open = True
            self._connection.commit()
            
    @prevent_concurrent(_bets_mutex)
    def close(self):
        self._connection.cursor().execute("UPDATE bets SET open=FALSE where id=?", str(self._id))
        self._open = False
        self._connection.commit()

    @property
    def open(self):
        return self._open

    @property
    def pot(self):
        return self._pot

    @prevent_concurrent(_bets_mutex)
    def update_pot(self, bet):
        pot = int(self._pot) + bet
        self._pot = str(pot)
        self._connection.cursor().execute("UPDATE bets SET pot=? where id=?", (self._pot, str(self._id)))
        self._connection.commit()

    def have_result(self):
        if self._result != 0:
            return True
        return False

    @prevent_concurrent(_bets_mutex)
    def set_result(self, result):
        self._connection.cursor().execute("UPDATE bets SET result=? where id=?", (result, self._id))
        self._result = result 
        self._connection.commit()   
    
    @staticmethod
    @prevent_concurrent(_bets_mutex)
    def get_all() -> list:
        all_bet = []
        cursor = sqlite3.connect('../../db/franc.db').cursor()
        cursor.execute("SELECT * from ?", (self._table,))
        for elem in self._connection.cursor().fetchall():
            all_bet.append(Bet(elem[0]))
        return all_bet        