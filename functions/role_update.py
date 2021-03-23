import re
from toolkit.authorizations import admin
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
    def run(message, name: str) -> str:
        salary = 0
        tmpId = 0
        for member in message.guild.members:
            if name == member.display_name or name == member.nick or name == member.name:
                for role in member.roles:
                    if Role(role.id).salary() >= salary:
                        tmpId = role.id
                        salary = Role(role.id).salary()
                account = Account(member.id)
                if not account.is_registered:
                    return f"La personne que vous cherchez à mettre à jour n'est pas enregistré dans la banque"
                account.update_role(tmpId)
                return f"Le role de {name} a bien été mis à jour"
            pass
        return f"La personne que vous avez spécifié ne semble pas être présente dans notre chère République"