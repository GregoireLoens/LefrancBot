class Gambler():
    _table = "gamblers"

    def __init__(self, account_id, bet_id)
        con = sqlite3.connect('../../db/franc.db')
        self._cursor = con.cursor()
        self._account_id = account_id
        self._bet_id = bet_id
        self._exist = False
        try:
            self._cursor.execute("SELECT bet_amount, choice from ? WHERE account_id = ? AND bet_id = ?", self._table, self.user_id, self.bet_id)
            self._bet_amount = self._cursor.fetchone[0]
            self._choice = self._cursor.fetchone[1]
            self._exist = True
        except:
            self.bet_amount = 0
            self._choice = None

    def has_already_bet(self):
        self._exist

    def bet_ammount(self):
        self._bet_amount

    def create(self, bet_amount, choice):
        self.cursor.execute("INSERT INTO ? (account_id, bet_id, bet_amount, choice) VALUES (?, ?, ?, ?);", self._table, self.user_id, self.bet_id, bet_ammount, choice)
        self.bet_amount = bet_amount
        self.choice = choice


