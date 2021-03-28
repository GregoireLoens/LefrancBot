import os
import importlib


class ArgumentError(Exception):
    """Raised when there is an error in the command arguments"""
    
    def __init__(self, msg="Une erreur est présente dans les paramètres de la commande.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class FunctionWrapper():

    _functions = {}

    def __init__(self):
        pass

    def load_functions(self):
        """
            Loads all the function from the "functions/" directory.
            The loaded functions will be callable from the discord server.
        """
        for file in os.listdir('./functions/'):
            if file.endswith('.py') and file != '__init__.py':
                module_name = 'functions.' + file[:-3]
                function = getattr(importlib.import_module(module_name), "Function")
                self._functions[function.command()] = function

    def call_function(self, message):
        """
            Call the function sent by discord if it exists.
            If not, returns a help message.
        """
        content = message.content.strip()
        cmd = content.split(' ')
        for f in self._functions.keys():
            if cmd[0] == f:
                try:
                    args = self._functions[f].parse_args(content[len(f):].strip())
                    if f == "!help":
                        return self._functions[f].run(self._functions, *args)
                    else:
                        return self._functions[f].run(message, *args)
                except Exception as e:
                    return str(e)
        return None