from toolkit.authorizations import admin
from models.Account import Account
from toolkit.discord import display_name_from_id

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!balance_all"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction renvoie le solde de tous les comptes en banque.\nUtilisation: !balance_all"

    @staticmethod
    def parse_args(line: str) -> list:
        return []

    @staticmethod
    @admin
    def run(message) -> str:
        balances = ""
        accounts = Account.get_all()
        for account in accounts:
            display_name = display_name_from_id(message, account.id)
            if not display_name:
                display_name = f"Unknown ({account.id})"
            balances += f"{display_name}: {account.balance}\n"
        return balances
