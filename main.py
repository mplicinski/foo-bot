import discord

from discord.ext import  commands
from dotenv import load_dotenv
from os import getenv

# loading token & (api keys)from enviroment file
load_dotenv()

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.reply("pong!")

# variable argument amount
@bot.command()
async def args(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

bot.run(getenv('TOKEN'))
