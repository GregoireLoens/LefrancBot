import discord
import os

client = discord.Client()

@client.event
async def on_message(message):
    if(message.content == '!salary'):
        #create adding once a month point func check role si admin donne a tout le monde
        #check pay date to ensure no multiple pay
        #7500 comissaire, 2500 garde, 2500 sommelier, 15000 tcheka
    elif(message.content == '!points'):
        #show points of the user
    elif(message.content == '!register'):
        #create account & give 200 points check role si commisaire ou président
    elif(message.content.startswith('!transfer')):
        #transfer money from one account to the other
        #Peuple ne peut pas donner d'argent aux immigrés & aux ennemis du peuple
    elif(message.content.startswith('!roleupdate')):
        #mettre a jour le role de la personne en param check role si commisaire ou président
    elif(message.content.startswith('!impots')):
        #retire de l'argent au compte du pseudo en param check role si commisaire ou président
    elif(message.content('!help')):
        #montre lhelp
    else:
        await message.channel.send("Désolé mais la commande demandé n'est pas disponible vous pouvez faire !help pour voir la liste des commandes")