import sqlite3
from models.Model import Model
from models.Role import Role


class AccountNotRegistered(Exception):
    """Raised when trying to perform a DB action with a non registered Account."""
    
    def __init__(self, msg="Le compte n'existe pas en base.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class Account(Model):

    _table = "comptes"

    def __init__(self, account_id: int, role_id: int = 0):
        super().__init__(account_id)
        self._balance = 0
        self._role_id = 0
        self._salary_date = 0
        try:
            self._cursor.execute("SELECT balance, role_id, salary_date FROM ? WHERE id = ?", self._table, self._id)
            res = self._cursor.fetchone()
            self._balance = res[0]
            self._role_id = res[1]
            self._salary_date = res[2]
            self._registered = True
        except:
            pass

    @staticmethod
    def get_all() -> list:
        ret = []
        cursor = sqlite3.connect('../../db/franc.db').cursor()
        for row in cursor.execute("SELECT id FROM ?", Account._table):
            ret.append(Account(row[0]))
        return ret

    def register(self):
        """
            Register the account in the database.
            If the account is already registered, do nothing.
        """
        if self.is_registered:
            # Already registered
            return
        self._cursor.execute(
            "INSERT INTO ? VALUES (?, ?, ?, ?)",
            self._table,
            self._id,
            self._balance,
            self._salary_date,
            self._role_id
        )
        self._cursor.commit()
        self._registered = True

    @property
    def balance(self) -> int:
        """Returns the current account balance"""
        self._balance

    def update_balance(self, ammount: int):
        """
            Update the account balance.
            Param MUST be a positive or negative integer.
        """
        if not self.is_registered:
            raise AccountNotRegistered()
        self._balance += ammount
        try:
            self._cursor.execute(
                "UPDATE ? SET balance = ? WHERE id = ?",
                self._table,
                self._balance,
                self._id
            )
            self._cursor.commit()
        except:
            self._balance -= ammount
            raise

    @property
    def role(self) -> Role:
        role = Role(self._role_id)
        if role.is_registered:
            return Role
        return None

    @property
    def salary_date(self):
        return self._salary_date

    def update_salary_date(self, date: int):
        if not self.is_registered:
            raise AccountNotRegistered()
        self._cursor.execute(
            "UPDATE ? SET salary_date = ? WHERE id = ?",
            self._table,
            date,
            self._id
        )
        self._cursor.commit()
        self._salary_date = date
