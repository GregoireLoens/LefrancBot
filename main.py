import discord
import os

from FunctionWrapper import FunctionWrapper
from config import DISCORD_TOKEN

FUNCTION_WRAPPER = FunctionWrapper()

FUNCTION_WRAPPER.load_functions()
intents = discord.Intents().default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author.id == 822477153643659394:
        return

    ret = FUNCTION_WRAPPER.call_function(message)
    if ret:
        await message.channel.send(ret)

client.run(DISCORD_TOKEN)
