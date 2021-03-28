import re
from toolkit.authorizations import admin
from toolkit.discord import id_from_display_name
from models.Account import Account
from FunctionWrapper import ArgumentError

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!transfer"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction vous permet de transférer de l'argent à un autre utilisateur.\nUtilisation: !transfert 'destinataire' montant"

    @staticmethod
    def parse_args(line: str) -> list:
        if not line:
            raise ArgumentError("Merci de spécifier les arguments de la commande.")

        match = re.match(r"['\"](?P<user>.+)['\"] (?P<value>\d+)", line)
        if not match:
            raise ArgumentError("Merci de bien vérifier que vous avez spécifié un montant ainsi qu'un destinataire pour votre transfert.")
        user = match.groupdict()['user']
        value = int(match.groupdict()['value'])
        return [user, value]

    @staticmethod
    def run(message,  to: str, value: int) -> str:
        account = Account(message.author.id)
        if not account.is_registered:
            return f"{message.author.display_name} n'existe pas dans notre banque."
        if value < 0:
            #notify admins
            return "Vous ne pouvez pas transférer un montant négatif voyons. Vous essayer d'arnaquer la banque ?"
        
        target_id = id_from_display_name(message, to)
        sec_account = Account(target_id)
        if not sec_account.is_registered:
            return f"{to} n'existe pas dans notre banque."

        account.update_balance(-value)
        sec_account.update_balance(value)
        return f"Le transfert d'un montant de {value} à bien été fait à {to}"