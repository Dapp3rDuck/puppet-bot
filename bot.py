import os
import os.path
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix="p!")
client.remove_command("help")
@client.event
async def on_ready():
    print("bot is ready")
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name="#general"
        )
    )

async def puppet():
    await client.wait_until_ready()
    channel = discord.Object(id='716037169072046114')
    while not client.is_closed:
        message = input(str(">>>"))
        await channel.send(message)

client.loop.create_task(puppet())
client.run(os.getenv("TOKEN"))
