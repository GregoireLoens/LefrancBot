import re
from toolkit.authorizations import admin
from toolkit.discord import member_from_display_name
from FunctionWrapper import ArgumentError
from models.Account import Account
from models.Role import Role


class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!register"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction ouvre un compte en baque aux utilisateurs spécifiés.\nUtilisation: !register '<name>' ['<name2>' ...]"

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
        def _format_output() -> str:
            message = ""
            if successful:
                message += "\nLes comptes suivants ont été créés avec succès :\n"
                for s in successful:
                    message += s + '\n'
            if errors:
                message += "\nLes comptes suivants n'ont pas pu être créés :\n"
                for (n, e) in errors:
                    message += n + ': ' + e + '\n'
            return message

        successful = []
        errors = []
        for name in names:
            tmpid = None
            salary = 0
            
            member = member_from_display_name(message, name)
            if member is None:
                errors.append((name, f"{name} ne semble pas être présent dans notre chère République."))
                continue

            for role in member.roles:
                if Role(role.id).salary >= salary:
                    tmpid = role.id
            if tmpid is None:
                errors.append((name, f"{name} ne semble pas encore avoir de role au sein de notre chère République."))
                continue
            account = Account(member.id, tmpid)
            account.register()
            account.update_balance(200)
            successful.append(name)

        return _format_output()
