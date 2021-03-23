from toolkit.authorizations import admin
from models.Account import Account
from FunctionWrapper import ArgumentError
import re

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!give"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction vous permet de transférer de l'argent à un autre utilisateur.\nUtilisation: !give 'destinataire' 'montant'"

    @staticmethod
    def parse_args(line: str) -> list:
        if not line:
            raise ArgumentError("L'argument 'nom' est manquant.")

        names = re.findall(r"((?<![\\])['\"])((?:.(?!(?<![\\])\1))*.?)\1", line)
        names = list(map(lambda x: x[1], names))
        names = list(filter(lambda x: x, names))
        if not names:
            raise ArgumentError("Merci de bien vérifier que vous avez spécifié un montant ainsi qu'un destinataire pour votre don")
        return [names]

    @staticmethod
    @admin
    def run(message, to: str, value: int) -> str:
        for member in message.guild.members:
            if to == member.display_name or to == member.nick or to == member.name:
                sec_account = Account(member.id)
                if not sec_account.is_registered:
                    return f"La personne à qui vous souhaitez offrir de l'argent n'existe pas dans notre banque."
                sec_account.update_balance(value)
                return f"La récompense d'un montant de {value} à bien été fait à {to}"
        return f"La personne que vous avez spécifié ne semble pas être présente dans notre chère République"