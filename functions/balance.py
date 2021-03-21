from toolkit.authorizations import admin
from models.Account import Account

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!balance"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction renvoie le de votre compte en baque.\nUtilisation: !balance"

    @staticmethod
    def parse_args(line: str) -> list:
        return []

    @staticmethod
    def run(message) -> str:
        account = Account(message.author.id)
        balance = account.balance
        return f"Le solde de votre compte est de {balance}"
