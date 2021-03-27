from toolkit.authorizations import admin
from models.Account import Account
from FunctionWrapper import ArgumentError
import re

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!transfer_from"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction vous permet de transférer de l'argent à un autre utilisateur.\nUtilisation: !transfert_from 'origine' 'destinataire' 'montant'"

    @staticmethod
    def parse_args(line: str) -> list:
        if not line:
            raise ArgumentError("Il n'y a pas d'argument après votre commande")

        names = re.findall(r"((?<![\\])['\"])((?:.(?!(?<![\\])\1))*.?)\1", line)
        names = list(map(lambda x: x[1], names))
        names = list(filter(lambda x: x, names))
        if not names:
            raise ArgumentError(
                "Merci de bien vérifier que vous avez spécifié un montant ainsi qu'une origine & un destinataire pour votre transfert ainsi qu'un montant")
        return [names]

    @staticmethod
    @admin
    def run(message, frm: str, to: str, value: int) -> str:
        frmId = 0
        toId = 0
        accounts = Account.get_all()
        for member in message.guild.members:
            if to == member.display_name or to == member.nick or to == member.name:
                toId = member.id
            elif frm == member.display_name or frm == member.nick or frm == member.name:
                frmId = member.id
            else:
                pass
        if toId == 0 or frmId == 0:
            return f"Un des membres spécifiés dans votre commande n'existe pas"
        frm_acc = Account(frmId)
        if not frm_acc.is_registered:
            "Le compte depuis lequel vous souhaitez forcé un débit n'existe pas"
        to_acc = Account(toId)
        if not to_acc.is_registered:
            "Le compte vers lequel vous souhaitez forcé un crédit n'existe pas"
        frm_acc.update_balance(-value)
        to_acc.update_balance(value)
        return f"Le transfert que vous souhaitiez effectué c'est bien passé, merci d'avoir utilisé nos services."