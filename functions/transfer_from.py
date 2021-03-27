import re
from toolkit.authorizations import admin
from toolkit.discord import id_from_display_name
from models.Account import Account
from FunctionWrapper import ArgumentError

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!transfer_from"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction vous permet de transférer de l'argent à un autre utilisateur.\nUtilisation: !transfert_from 'origine' 'destinataire' montant"

    @staticmethod
    def parse_args(line: str) -> list:
        if not line:
            raise ArgumentError("Il n'y a pas d'argument après votre commande")

        match = re.match(r"['\"](?P<frm>.+)['\"] ['\"](?P<to>.+)['\"] (?P<value>\d+)", line)
        if not match:
            raise ArgumentError("Merci de bien vérifier que vous avez spécifié un montant ainsi qu'un destinataire pour votre transfert.")
        frm = match.groupdict()['frm']
        to = match.groupdict()['to']
        value = int(match.groupdict()['value'])
        return [frm, to, value]

    @staticmethod
    @admin
    def run(message, frm: str, to: str, value: int) -> str:
        frmId = id_from_display_name(message, frm)
        toId = id_from_display_name(message, to)
        frm_acc = Account(frmId)
        if not frm_acc.is_registered:
            "Le compte depuis lequel vous souhaitez forcé un débit n'existe pas"
        to_acc = Account(toId)
        if not to_acc.is_registered:
            "Le compte vers lequel vous souhaitez forcé un crédit n'existe pas"
        frm_acc.update_balance(-abs(value))
        to_acc.update_balance(abs(value))
        return f"Le transfert que vous souhaitiez effectué c'est bien passé, merci d'avoir utilisé nos services."