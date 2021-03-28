import sqlite3


class Model():

    _table = None # This needs to be overloaded

    def __init__(self, id):
        self._id = id
        self._registered = False
        self._connection = sqlite3.connect('../../db/franc.db')

    @property
    def is_registered(self) -> bool:
        """Returns True if the Account is registered in the DB, False otherwise."""
        return self._registered

    @property
    def id(self) -> int:
        return self._id

    def register(self):
        raise NotImplementedError("This Model method needs to be override!")

    @staticmethod
    def get_all() -> list:
        raise NotImplementedError("This Model method needs to be override!")
