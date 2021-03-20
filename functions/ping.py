from toolkit.authorizations import admin

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!ping"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction renvoie le message passé en paramètre ou 'pong' si le message est absent.\nUtilisation: !ping <message>"

    @staticmethod
    def parse_args(line: str) -> list:
        """
            Parse the given arguments.
            The received line is already free of the command and trailing spaces.
        """
        if line:
            return [line]
        else:
            return ['pong']

    @staticmethod
    # You could add the @admin decorator here to restrict privileges
    def run(message, arg1: str) -> str:
        """
            Execute the function and return the message to send back to the discord server.

            The 'message' parameter is a discord message object.
            
            The parameters from arg1 to argN are corresponding to the list returned by the 'parse_args' method.
            You can name the parameters as you want.
        """
        return arg1
