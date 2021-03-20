import discord
import os

from FunctionWrapper import FunctionWrapper

FUNCTION_WRAPPER = FunctionWrapper()

FUNCTION_WRAPPER.load_functions()
client = discord.Client()

@client.event
async def on_message(message):
    if message.author.id == 822477153643659394:
        return

    ret = FUNCTION_WRAPPER.call_function(message)
    await message.channel.send(ret)

client.run(os.getenv("DTOKEN"))
