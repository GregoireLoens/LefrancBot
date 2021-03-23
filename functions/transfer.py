from toolkit.authorizations import admin
from models.Account import Account
from FunctionWrapper import ArgumentError
import re

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!transfer"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction vous permet de transférer de l'argent à un autre utilisateur.\nUtilisation: !transfert 'destinataire' 'montant'"

    @staticmethod
    def parse_args(line: str) -> list:
        if not line:
            raise ArgumentError("L'argument 'nom' est manquant.")

        names = re.findall(r"((?<![\\])['\"])((?:.(?!(?<![\\])\1))*.?)\1", line)
        names = list(map(lambda x: x[1], names))
        names = list(filter(lambda x: x, names))
        if not names:
            raise ArgumentError("Merci de bien vérifier que vous avez spécifié un montant ainsi qu'un destinataire pour votre transfert")
        return [names]

    @staticmethod
    def run(message,  to: str, value: int) -> str:
        account = Account(message.author.id)
        if not account.is_registered:
            return "Vous semblez ne pas avoir de compte chez nous. Contactez un administrateur pour en ouvrir un !"
        if value < 0:
            #notify admins
            return "Vous ne pouvez pas transférer un montant négatif voyons."
        account.update_balance(-value)
        for member in message.guild.members:
            if to == member.display_name or to == member.nick or to == member.name:
                sec_account = Account(member.id)
                if not sec_account.is_registered:
                    return "Le compte vers lequel vous souhaitez effectué un transfert semble ne pas exister. N'hésitez pas à lui dire de contacter un administrateur pour se créer un compte"
                sec_account.update_balance(value)
                return f"Le transfert d'un montant de {value} à bien été fait à {to}"
        return f"La personne que vous avez spécifié ne semble pas être présente dans notre chère république!"