import sqlite3
from models.Model import Model
from config import SQLITE_DB_PATH


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
            cur = self._connection.cursor()
            cur.execute("SELECT salary FROM roles WHERE id = ?", (self._id,))
            self._salary = cur.fetchone()[0]
            self._registered = True
        except:
            pass

    @staticmethod
    def get_all() -> list:
        ret = []
        cursor = sqlite3.connect(SQLITE_DB_PATH).cursor()
        for row in cursor.execute("SELECT id FROM roles"):
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
        self._connection.cursor().execute("INSERT INTO roles (id, salary) VALUES (?, ?)", (self._id, self._salary))
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
            "UPDATE roles SET salary = ? WHERE id = ?",
            (salary, self._id)
        )
        self._connection.commit()
        self._salary = salary
