import os
import importlib


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
        for f in self._functions.keys():
            if content.startswith(f):
                try:
                    args = self._functions[f].parse_args(content[len(f):].strip())
                    return self._functions[f].run(message, *args)
                except Exception as e:
                    return str(e)
        return "Cette commande n'existe pas. Entrez '!help' pour voir la liste des commandes disponibles."