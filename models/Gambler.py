import sqlite3
from models.Model import Model
from config import SQLITE_DB_PATH

class Gambler(Model):
    _table = "gamblers"

    def __init__(self, account_id, bet_id):
        super().__init__(0)
        self._exist = False
        self._bet_id = bet_id
        self._account_id = account_id
        try:
            cur = self._connection.cursor().execute("SELECT bet_amount, choice from gamblers WHERE account_id = ? AND bet_id = ?", (self._account_id, self._bet_id))
            self._bet_amount, self._choice = cur.fetchone()
            self._exist = True
        except:
            self.bet_amount = 0
            self._choice = None

    @property
    def exist(self):
        return self._exist

    @property
    def bet_ammount(self):
        return self._bet_amount
    
    @property
    def account_id(self):
        return self._account_id

    def create(self, bet_amount, choice):
        self._connection.cursor().execute("INSERT INTO gamblers (account_id, bet_id, bet_amount, choice) VALUES (?, ?, ?, ?);", (self._account_id, self._bet_id, bet_amount, choice))
        self._bet_amount = bet_amount
        self._choice = choice
        self._connection.commit()

    @staticmethod
    def get_all_winner(bet_id, result):
        cursor = sqlite3.connect(SQLITE_DB_PATH).cursor()
        cursor.execute("SELECT * from gamblers WHERE bet_id=? AND choice=?", (bet_id, result))
        all_gamblers = cursor.fetchall()
        return all_gamblers