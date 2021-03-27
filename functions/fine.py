import re
from toolkit.authorizations import admin
from toolkit.discord import id_from_display_name
from models.Account import Account
from FunctionWrapper import ArgumentError

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!fine"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction vous permet de faire payer une ammende à un utilisateur.\nUtilisation: !fine 'utilisateur' montant"

    @staticmethod
    def parse_args(line: str) -> list:
        if not line:
            raise ArgumentError("Merci de spécifier les arguments de la commande")

        match = re.match(r"['\"](?P<user>.+)['\"] (?P<value>\d+)", line)
        if not match:
            raise ArgumentError("Merci de bien vérifier que vous avez spécifié un montant ainsi qu'un utilisateur pour votre amende")
        user = match.groupdict()['user']
        value = int(match.groupdict()['value'])
        return [user, value]

    @staticmethod
    @admin
    def run(message, user: str, value: int) -> str:
        member_id = id_from_display_name(message, user)
        if member_id == -1:
            return f"{user} ne semble pas être présent dans notre chère République"

        account = Account(member_id)
        if not account.is_registered:
            return f"{user} n'existe pas dans notre banque."

        account.update_balance(-abs(value)) # abs() is used to ensure the intended operation is done
        return f"L'amende d'un montant de {value} à bien été appliquée à {user}."