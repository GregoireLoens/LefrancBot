import discord
import db
from datetime import date

#!salary
    # create adding once a month point func check role si admin donne a tout le monde
    # check pay date to ensure no multiple pay
    # 7500 comissaire, 2500 garde, 2500 sommelier, 15000 tcheka

def salary(cur, message):
    today = date.today()
    admin = False
    str = ''
    for role in (message.author.roles):
        if (role.name == 'Président Général' or role.name == 'Commissariat du peuple'):
            admin = True
    if admin:
        data = db.get_salaries(cur)
        for user in data:
            if (user[1] != today.month):
                db.add_points(cur, user[0], user[2])
                db.update_month(cur, user[0], today.month)
    else:
        str = "You don't have the rights to use this command"
    return str

#!points
    # show points of the user
def show_francs(cur, message):
    return (db.check_account(cur, message))

#!register
    # create account & give 200 points check role si commisaire ou président
def register_members(cur, message):
    """data = message.content.split('/')
    for name in data:
        if (name.starstwith('!') or not name):
            pass
        else:
            toto = messsage.guild.members
            for member in toto:
                if member.name =
            #get discord member to register id"""

def register_roles(cur, message):
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
        db.register_roles(cur, (salary, role.id))

    #!transfer
    # transfer money from one account to the other
    # Peuple ne peut pas donner d'argent aux immigrés & aux ennemis du peuple

    #!roleupdate
    # mettre a jour le role de la personne en param check role si commisaire ou président

    #!impots
    # retire de l'argent au compte du pseudo en param check role si commisaire ou président

    #!help
    # montre lhelp