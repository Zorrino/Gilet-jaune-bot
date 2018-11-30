import discord
import asyncio
from random import *

client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as :", client.user.name)
    print("ID : ", client.user.id)

@client.event
async def on_message(message):
    if message.content == "gilet jaune":
        await client.send_file(message.channel, "giletjaune.jpg")
        
client.run("NO :)")
