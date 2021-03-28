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
        return "!role_update"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction enregistre un nouvel utilisateur en base.\nUtilisation: !role_update '<name>'"

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
        return names


    @staticmethod
    @admin
    def run(message, names: list) -> str:
        def _format_output() -> str:
            message = ""
            if successful:
                message += "\nLes comptes suivants ont été mis à jour avec succès :\n"
                for s in successful:
                    message += s + '\n'
            if errors:
                message += "\nLes comptes suivants n'ont pas pu être mis à jour :\n"
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
                if Role(role.id).salary() > salary:
                    tmpid = role.id
            if tmpid is None:
                errors.append((name, f"{name} ne semble pas encore avoir de role au sein de notre chère République."))
                continue

            account = Account(member.id)
            if not account.is_registered:
                errors.append((name, f"{name} n'existe pas dans notre banque."))
                continue
            
            try:
                account.update_role(tmpid)
            except Exception as e:
                errors.append((name, str(e)))
                continue

            successful.append(name)
        return _format_output()
