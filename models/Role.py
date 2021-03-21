import sqlite3
from models.Model import Model


class RoleNotRegistered(Exception):
    """Raised when trying to perform a DB action with a non registered Role."""
    
    def __init__(self, msg="Le role n'existe pas en base.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class Role(Model):

    _table = "roles"

    def __init__(self, role_id: int, salary: int = 0):
        super().__init__(role_id)
        self._salary = salary
        self._registered = False
        try:
            self._connection.cursor().execute("SELECT salary FROM ? WHERE id = ?", self._table, self._id)
            self._salary = self._connection.cursor().fetchone()[0]
        except:
            pass

    @staticmethod
    def get_all() -> list:
        ret = []
        cursor = sqlite3.connect('../../db/franc.db').cursor()
        for row in cursor.execute("SELECT id FROM ?", Role._table):
            ret.append(Role(row[0]))
        return ret

    def register(self):
        """
            Register the role in the database.
            If the role is already registered, do nothing.
        """
        if self._registered:
            # Already registered
            return
        self._connection.cursor().execute(
            "INSERT INTO ? (id, salary) VALUES (?, ?)",
            self._table,
            self._id,
            self._salary
        )
        self._connection.commit()
        self._registered = True

    @property
    def salary(self):
        return self._salary

    def update_salary(self, salary: int):
        """
            Update the role salary.
            Param MUST be a positive integer.
        """
        if not self.is_registered:
            raise RoleNotRegistered(f"Le role avec l'id {self._id} n'existe pas en base.")
        self._connection.cursor().execute(
                "UPDATE ? SET salary = ? WHERE id = ?",
                self._table,
                self._salary,
                self._id
            )
        self._connection.commit()
        self._salary = salary
