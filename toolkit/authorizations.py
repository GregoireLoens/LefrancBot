

ADMIN_ROLES = [
    'Président Général',
    'Commissariat du peuple',
    'Garde du corps',
]

class UnsuficientPrivileges(Exception):
    """Raised when the caller does not have sufficient permitions (Role) to use the funtion."""
    
    def __init__(self, msg="Vous n'avez pas les privilèges suffisants pour lancer cette commande.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

def admin(func):
    def function_wrapper(message, *args, **kwargs):
        for role in (message.author.roles):
            if role.name in ADMIN_ROLES:
                return func(message, *args, **kwargs)
        raise UnsuficientPrivileges(f"Lancer cette commande demande un des rôles suivants : {ADMIN_ROLES}")

    return function_wrapper
