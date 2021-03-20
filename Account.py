import sqlite3

class Account():

    _table = "comptes"

    def __init__(self, account_id: str):
        con = sqlite3.connect('../../db/franc.db')
        self._cursor = con.cursor()
        self._account_id = account_id
        self._registered = False
        try:
            self._cursor.execute("SELECT francs FROM ? WHERE account_id = ?", self._table, self._account_id)
            self._balance = self._cursor.fetchone()[0]
            self._registered = True
        except:
            self._balance = 0

    def balance(self) -> int:
        """
            Returns the current account balance
        """
        self._balance

    def register(self):
        """
            Register the account in the database.
            If the account is already registered, do nothing.
        """
        if self._registered:
            # Already registered
            return
        self._cursor.execute(
            "INSERT INTO ? (account_id, francs) VALUES (?, ?)",
            self._table,
            self._account_id,
            self._balance
        )
        self._cursor.commit()
        self._registered = True

    def update_balance(self, ammount: int):
        """
            Update the account balance.
            Param MUST be a positive or negative integer.
        """
        self.balance += ammount
        try:
            self._cursor.execute(
                "UPDATE ? SET francs = ? WHERE account_id = ?",
                self._table,
                self._balance,
                self._account_id
            )
            self._cursor.commit()
        except:
            self.balance -= ammount
            raise
