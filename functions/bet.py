import re
from FunctionWrapper import ArgumentError
from models.Bet import Bet
from models.Gambler import Gambler
from models.Account import Account

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!bet"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return """La commande permet parier.\nUtilisation: !bet id_pari id_choix montant (ex: !bet 1 2 200) """

    @staticmethod
    def parse_args(line: str) -> list:
        """
            Parse the given arguments.
            The received line is already free of the command and trailing spaces.
        """
        arg_list = re.findall("([0-9])\s([0-9])\s([0-9]*$)", line)
        if not arg_list:
            raise  ArgumentError("Il y a un problème dans votre commandes, vos arguments ne sont pas valides")
        return arg_list[0]

    @staticmethod
    def run(message, bet_id: int, choice: int, amount: int) -> str:
        """
            Execute the function and return the message to send back to the discord server.

            The 'message' parameter is a discord message object.
            
            The parameters from arg1 to argN are corresponding to the list returned by the 'parse_args' method.
            You can name the parameters as you want.
        """
        bet = Bet(bet_id)
        if bet.open:
            gambler = Gambler(message.author.id, bet_id)
            if gambler.exist:
                return "Vous avez déjà misé sur ce pari"
            else:
                account = Account(message.author.id)
                account.update_balance(int(amount) * (-1))
                gambler.create(amount, choice)   
                return "Vous avez parié {0} francs sur le Pari numéro {1}, bonne chance !".format(amount, bet_id)
        else:
            return "Le pari est fermé vous ne pouvez plus miser"