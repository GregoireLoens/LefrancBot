from toolkit.authorizations import admin

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!help"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction renvoie le message d'aide de la commande indiquée.\nUtilisation: !help <commande>"

    @staticmethod
    def parse_args(line: str) -> list:
        """
            Parse the given arguments.
            The received line is already free of the command and trailing spaces.
        """
        if line:
            return [line]
        else:
            return []

    @staticmethod
    def run(functions: dict, command: str = None) -> str:
        if not command:
            return "Voici les commandes disponibles :\n" + '\n'.join(functions.keys())
        
        function = functions.get(command, None)
        if function is None:
            return "Merci de donner le nom d'une fonction existante.\nTapez !help pour avoir la liste des commandes disponibles."
        return function.help()

