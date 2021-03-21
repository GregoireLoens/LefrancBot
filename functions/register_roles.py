from toolkit.authorizations import admin
from models.Role import Role

class Function():

    @staticmethod
    def command() -> str:
        """Returns the command to call the current function."""
        return "!register_roles"

    @staticmethod
    def help() -> str:
        """Returns the help string to send back to the discord."""
        return "La fonction enregistre les roles en base avec le salaire assoié.\nUtilisation: !register_roles"

    @staticmethod
    def parse_args(line: str) -> list:
        return []

    @staticmethod
    # You could add the @admin decorator here to restrict privileges
    def run(message) -> str:
        for role in message.guild.roles:
            if (role.name == 'Tchéka'):
                salary = 15000
            elif (role.name == 'Commissariat du peuple'):
                salary = 7500
            elif (role.name == "Sommelier de l'élysée"):
                salary = 2500
            elif (role.name == "Garde du corp"):
                salary = 2500
            elif (role.name == "Peuple Souverain"):
                salary = 500
            else:
                salary = 0
            Role(role.id, salary).register()
        return "Les rôles ont bien été enregistrés."
