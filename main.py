import discord
import os
from db import connect_db
from bet import create_bet

client = discord.Client()
cur = connect_db()

@client.event
async def on_message(message):
    content = message.content.split("/")
    if content[0] == '!ping':
        await message.channel.send('pong')
    elif '!createbet' in content[0]:
        await message.channel.send(create_bet(cur, content[1], [content[2], content[3]]))
    #elif(message.content == '!weekly'):
        #create adding once a month point func check role si admin donne a tout le monde
        #check pay date to ensure no multiple pay
        #7500 comissaire, 2500 garde, 2500 sommelier, 15000 tcheka
    #elif(message.content == '!points'):
        #show points of the user
    #elif(message.content == '!register'):
        #create account & give 200 points check role si commisaire ou président
    #elif(message.content.startswith('!transfer')):
        #transfer money from one account to the other
        #Peuple ne peut pas donner d'argent aux immigrés & aux ennemis du peuple
    #elif(message.content.startswith('!roleupdate')):
        #mettre a jour le role de la personne en param check role si commisaire ou président
    #elif(message.content.startswith('!impots')):
        #retire de l'argent au compte du pseudo en param check role si commisaire ou président
    #elif(message.content('!help')):
        #montre lhelp
    #else:
    #    await message.channel.send("Désolé mais la commande demandé n'est pas disponible vous pouvez faire !help pour voir la liste des commandes")

client.run(os.getenv("DTOKEN"))
