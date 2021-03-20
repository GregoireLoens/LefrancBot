import discord
from Account import Account


#!salary
    # create adding once a month point func check role si admin donne a tout le monde
    # check pay date to ensure no multiple pay
    # 7500 comissaire, 2500 garde, 2500 sommelier, 15000 tcheka
@admin
def salary(message):
    account = Account(message.author.id)


#!points
    # show points of the user
def show_francs(cur, message):
    return (db.check_account(cur, message))

#!register
    # create account & give 200 points check role si commisaire ou président
def register_members(cur, message):
    str = register_members_in_db(cur, message)
    
    #!transfer
    # transfer money from one account to the other
    # Peuple ne peut pas donner d'argent aux immigrés & aux ennemis du peuple

    #!roleupdate
    # mettre a jour le role de la personne en param check role si commisaire ou président

    #!impots
    # retire de l'argent au compte du pseudo en param check role si commisaire ou président

    #!help
    # montre lhelp
