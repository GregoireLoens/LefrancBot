import re
from toolkit.authorizations import admin
from FunctionWrapper import ArgumentError
from models.Account import Account

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!register"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction enregistre un nouvel utilisateur en base.\nUtilisation: !register '<name>' ['<name2>' ...]"

    @staticmethod
    def parse_args(line: str) -> list:
        """
            Parse the given arguments.
            The received line is already free of the command and trailing spaces.
        """
        if not line:
            raise ArgumentError("L'argument 'nom' est manquant.")

        names = re.findall(r"((?<![\\])['\"])((?:.(?!(?<![\\])\1))*.?)\1", line)
        names = list(map(lambda x: x[1], names))
        names = list(filter(lambda x: x, names))
        if not names:
            raise ArgumentError("Merci de fournir un nom correctement formaté.")
        return [names]


    @staticmethod
    @admin
    def run(message, names: list) -> str:
        for name in names:
            # Get the discord id corresponding to the name
            # Get the role id of the member
            # account = Account(account_id, role_id)
            # account.register()
            # account.update_balance(200)
            pass
        return str(names)
        return "Cette fonction n'est pas encore implémentée"
