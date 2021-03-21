from toolkit.authorizations import admin
from datetime import date
from models.Account import Account
from models.Role import Role

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!salary"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction déclenche le versement mensuel des salaires.\nUtilisation: !salary"

    @staticmethod
    def parse_args(line: str) -> list:
        return []

    @staticmethod
    @admin
    def run(message) -> str:
        today = date.today()
        accounts = Account.get_all()
        for account in accounts:
            role = account.role
            if role and account.salary_date != today.month:
                account.update_balance(role.salary)
                account.update_month(today.month)

        return "Le salaire a bien été versé.")
