import sqlite3


class NotRegistered(Exception):
    """Raised when trying to perform a DB action with a non registered Account."""
    
    def __init__(self, msg="Le compte n'existe pas en base.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class Account():

    _table = "comptes"

    def __init__(self, account_id: str, role_id: int = 0):
        con = sqlite3.connect('../../db/franc.db')
        self._cursor = con.cursor()
        self._account_id = account_id
        self._balance = 0
        self._role_id = 0
        self._salary_date = 0
        self._registered = False
        try:
            self._cursor.execute("SELECT balance, role_id, salary_date FROM ? WHERE account_id = ?", self._table, self._account_id)
            res = self._cursor.fetchone()
            self._balance = res[0]
            self._role_id = res[1]
            self._salary_date = res[2]
            self._registered = True
        except:
            pass

    def balance(self) -> int:
        """Returns the current account balance"""
        self._balance

    def is_registered(self):
        """Returns True if the Account is registered in the DB, False otherwise."""
        return self._registered

    def register(self):
        """
            Register the account in the database.
            If the account is already registered, do nothing.
        """
        if self._registered:
            # Already registered
            return
        self._cursor.execute(
            "INSERT INTO ? VALUES (?, ?, ?, ?)",
            self._table,
            self._account_id,
            self._balance,
            self._salary_date,
            self._role_id
        )
        self._cursor.commit()
        self._registered = True

    def update_balance(self, ammount: int):
        """
            Update the account balance.
            Param MUST be a positive or negative integer.
        """
        if not self.is_registered():
            raise NotRegistered()
        self.balance += ammount
        try:
            self._cursor.execute(
                "UPDATE ? SET balance = ? WHERE account_id = ?",
                self._table,
                self._balance,
                self._account_id
            )
            self._cursor.commit()
        except:
            self.balance -= ammount
            raise
