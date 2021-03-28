import re
from FunctionWrapper import ArgumentError

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!bet"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return """La commande permet parier.\nUtilisation: !bet montant (ex: !bet 200) """

    @staticmethod
    def parse_args(line: str) -> list:
        """
            Parse the given arguments.
            The received line is already free of the command and trailing spaces.
        """
        arg_list = re.findall("([0-9])\s([0-9]*$)", line)
        print(arg_list)
        if not arg_list:
            raise  ArgumentError("Il y a un problème dans votre commandes, vos arguments ne sont pas valides")
        return arg_list[0]

    @staticmethod
    def run(message, bet_id: int, amount: id) -> str:
        """
            Execute the function and return the message to send back to the discord server.

            The 'message' parameter is a discord message object.
            
            The parameters from arg1 to argN are corresponding to the list returned by the 'parse_args' method.
            You can name the parameters as you want.
        """

        return "Vous avez parié {0} francs sur le Pari numéro {1}, bonne chance !".format(amount, bet_id)