from toolkit.authorizations import admin
from models.Account import Account

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
            for member in message.guild.members:
                if account.id == member.id:
                    balances += f"{member.display_name}: {account.balance}\n"
        return balances
