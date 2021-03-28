import re
from FunctionWrapper import ArgumentError
from models.Bet import Bet

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!createbet"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return """La commande permet de créer un paris.\nUtilisation: !createbet "intitulé du paris" choix 1 choix 2"""

    @staticmethod
    def parse_args(line: str) -> list:
        """
            Parse the given arguments.
            The received line is already free of the command and trailing spaces.
        """
        arg_list = re.findall("^(\".*\")\s(\".*\")\s(\".*\")", line)
        if not arg_list:
            raise  ArgumentError("Il y a un problème dans votre commandes, vos arguments ne sont pas valides")
        return arg_list[0]

    @staticmethod
    def run(message, subject: str, f_choice: str, s_choice: str) -> str:
        """
            Execute the function and return the message to send back to the discord server.

            The 'message' parameter is a discord message object.
            
            The parameters from arg1 to argN are corresponding to the list returned by the 'parse_args' method.
            You can name the parameters as you want.
        """
        bet = Bet()
        if not bet.open:
            return "Votre pari n'a pas pu être crée en base"
        return "Le Pari numéro {0} est créé.\nSujet :{1}\n-> choix 1: {2}\n-> choix 2: {3}".format(bet.id, subject, f_choice, s_choice)