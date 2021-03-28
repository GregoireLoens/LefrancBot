import re
from FunctionWrapper import ArgumentError
from models.Bet import Bet
from models.Gambler import Gambler
from models.Account import Account

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!betresult"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return """La commande permet de publier un résultat de pari.\nUtilisation: !betresult id_pari id_résultat (ex: !betresult 1 2) """

    @staticmethod
    def parse_args(line: str) -> list:
        """
            Parse the given arguments.
            The received line is already free of the command and trailing spaces.
        """
        arg_list = re.findall("([0-9])\s([0-9]*$)", line)
        if not arg_list:
            raise  ArgumentError("Il y a un problème dans votre commandes, vos arguments ne sont pas valides")
        return arg_list[0]

    @staticmethod
    def run(message, bet_id: int, result: int) -> str:
        """
            Execute the function and return the message to send back to the discord server.

            The 'message' parameter is a discord message object.
            
            The parameters from arg1 to argN are corresponding to the list returned by the 'parse_args' method.
            You can name the parameters as you want.
        """
        bet = Bet(bet_id)
        if bet.open:
            return "Le pari n'est pas fermé, fermez le pari avant de publier le résultat"
        if bet.have_result():
            return "Les résultats sont déjà tombé"
        else:
            bet.set_result(result)
            gamblers = Gambler.get_all_winner(bet_id, result)
            win = bet.pot / len(gamblers)
            for elem in gamblers:
                Account(elem[1]).update_balance(win)
        return "Les résultats du paris {0} sont tombés, {1} francs vont être versés aux gagnants".format(bet_id, win)