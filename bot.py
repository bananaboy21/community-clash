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
    em = discord.Embed(color=ctx.author.color, title="Community Clash Bot Help")
    for x in bot.commands:
        em.add_field(name=x.signature, value=x.short_doc, inline=False)
    await ctx.send(embed=em)
    
    
    
@bot.command()
async def th9winner(ctx):
    await ctx.send("""
**Hall of fame th9**
chandan|ww999 & sky09 foreverheart_eyes#4055
""")
    
    
bot.run(os.environ.get("TOKEN"))
