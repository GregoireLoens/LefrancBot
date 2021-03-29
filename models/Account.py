import sqlite3
from toolkit.db import prevent_concurrent
from threading import Lock
from models.Model import Model
from models.Role import Role

# Lock used to prevent conccurent acces to the same table into the database
_accounts_mutex = Lock()

class AccountNotRegistered(Exception):
    """Raised when trying to perform a DB action with a non registered Account."""
    
    def __init__(self, msg="Le compte n'existe pas en base.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class Account(Model):

    _table = "accounts"

    @prevent_concurrent(_accounts_mutex)
    def __init__(self, account_id, role_id: int = 0):
        super().__init__(account_id)
        self._balance = 0
        self._role_id = role_id
        self._salary_date = 0
        cursor = self._connection.cursor()
        try:
            cursor.execute(
                "SELECT balance, role_id, salary_date FROM accounts WHERE id = ?",
                (self._id,)
            )
            res = cursor.fetchone()
            self._balance = res[0]
            self._role_id = res[1]
            self._salary_date = res[2]
            self._registered = True
        except:
            pass

    @staticmethod
    @prevent_concurrent(_accounts_mutex)
    def get_all() -> list:
        ret = []
        cursor = sqlite3.connect('../../db/franc.db').cursor()
        for row in cursor.execute("SELECT id FROM accounts"):
            ret.append(Account(row[0]))
        return ret

    @prevent_concurrent(_accounts_mutex)
    def register(self):
        """
            Register the account in the database.
            If the account is already registered, do nothing.
        """
        if self.is_registered:
            # Already registered
            return
        self._connection.cursor().execute(
            "INSERT INTO accounts (id, balance, salary_date, role_id) VALUES (?, ?, ?, ?)",
            (self._id, self._balance, self._salary_date, self._role_id)
        )
        self._connection.commit()
        self._registered = True

    @property
    def balance(self) -> int:
        """Returns the current account balance"""
        return self._balance

    @prevent_concurrent(_accounts_mutex)
    def update_balance(self, ammount: int):
        """
            Update the account balance by adding to the current value.
            Param MUST be a positive or negative integer.
        """
        if not self.is_registered:
            raise AccountNotRegistered()
        self._balance += ammount
        try:
            self._connection.cursor().execute(
                "UPDATE accounts SET balance = ? WHERE id = ?",
                (self._balance, self._id)
            )
            self._connection.commit()
        except:
            self._balance -= ammount
            raise

    @property
    def role(self) -> Role:
        role = Role(self._role_id)
        if role.is_registered:
            return role
        return None

    @property
    def salary_date(self):
        return self._salary_date

    @prevent_concurrent(_accounts_mutex)
    def update_salary_date(self, date: int):
        if not self.is_registered:
            raise AccountNotRegistered()
        self._connection.cursor().execute(
            "UPDATE accounts SET salary_date = ? WHERE id = ?",
            (date, self._id)
        )
        self._connection.commit()
        self._salary_date = date

    @prevent_concurrent(_accounts_mutex)
    def update_role(self, id: int):
        if not self.is_registered:
            raise AccountNotRegistered()
        self._connection.cursor().execute(
            "UPDATE accounts SET role_id = ? WHERE id = ?",
            (id, self._id)
        )
        self._connection.commit()
        self._role_id = id