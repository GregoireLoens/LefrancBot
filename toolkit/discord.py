

def member_from_display_name(message, display_name: str):
    """Return the member object corresponding to the given diplay name or None"""
    for member in message.guild.members:
        if display_name == member.display_name or display_name == member.nick or display_name == member.name:
            return member
    return None

def member_from_id(message, member_id: int):
    """Return the member object corresponding to the given id or None"""
    for member in message.guild.members:
        if member_id == member.id:
            return member
    return None

def display_name_from_id(message, member_id: int) -> str:
    """Return the member diplay name corresponding to the given id or None"""
    member = member_from_id(message, member_id)
    if member:
        return member.display_name
    return None

def id_from_display_name(message, display_name: str) -> int:
    """Return the member id corresponding to the given diplay name or -1"""
    member = member_from_display_name(message, display_name)
    if member:
        return member.id
    return -1
