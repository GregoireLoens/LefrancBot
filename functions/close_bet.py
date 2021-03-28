import re
from FunctionWrapper import ArgumentError
from models.Bet import Bet

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!closebet"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return """La commande permet de fermer un pari.\nUtilisation: !closebet id"""

    @staticmethod
    def parse_args(line: str) -> list:
        """
            Parse the given arguments.
            The received line is already free of the command and trailing spaces.
        """
        arg_list = re.findall("^\d", line)
        if not arg_list:
            raise  ArgumentError("Il ya un problème dans votre commandes, vos arguments ne sont pas valides")
        print(arg_list)
        return  arg_list

    @staticmethod
    def run(message, bet_id: str) -> str:
        """
            Execute the function and return the message to send back to the discord server.

            The 'message' parameter is a discord message object.
            
            The parameters from arg1 to argN are corresponding to the list returned by the 'parse_args' method.
            You can name the parameters as you want.
        """
        bet = Bet(int(bet_id))
        bet.close()
        return "Paris numéro {0} fermé".format(int(bet_id))