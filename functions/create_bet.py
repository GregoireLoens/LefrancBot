import re
from FunctionWrapper import ArgumentError
from FunctionWrapper import ArgumentError

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
            raise  ArgumentError("Il ya un problème dans votre commandes, vos arguments ne sont pas valides")
        return  arg_list

    @staticmethod
    def run(message, arg_list: list) -> str:
        """
            Execute the function and return the message to send back to the discord server.

            The 'message' parameter is a discord message object.
            
            The parameters from arg1 to argN are corresponding to the list returned by the 'parse_args' method.
            You can name the parameters as you want.
        """
        return "sujet :{0}\n-choix 1: {1}\n-choix 2: {2}".format(arg_list[0], arg_list[1], arg_list[2])