import discord
import os
from discord.ext import commands


bot = commands.Bot(command_prefix="%",owner_id=277981712989028353)
bot.remove_command("help")


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    await bot.change_presence(activity=discord.Game(name="%help for help!"))
    
    
@bot.command()
async def help(ctx):
    
