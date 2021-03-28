import sqlite3
from models.Model import Model

class Gambler(Model):
    _table = "gamblers"

    def __init__(self, account_id, bet_id):
        self._exist = False
        try:
            cur = self._connection.cursor().execute("SELECT bet_amount, choice from gamblers WHERE account_id = ? AND bet_id = ?", self.user_id, self.bet_id)
            self._bet_amount = cur.fetchone[0]
            self._choice = cur.fetchone[1]
            self._exist = True
        except:
            self.bet_amount = 0
            self._choice = None

    @property
    def exist(self):
        self._exist

    @property
    def bet_ammount(self):
        self._bet_amount

    def create(self, bet_amount, choice):
        self._connection.cursor().execute("INSERT INTO ? (account_id, bet_id, bet_amount, choice) VALUES (?, ?, ?, ?);", self._table, self.user_id, self.bet_id, bet_ammount, choice)
        self.bet_amount = bet_amount
        self.choice = choice

    @staticmethod
    def get_all():
        return 0