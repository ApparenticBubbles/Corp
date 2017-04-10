import discord

from discord.ext import commands

description = 'Corp Bot made by ApparenticBubbles.'
bot_prefix  =  'corp?'

client = commands.Bot(description=description, command_prefix=bot_prefix)

@client.event
async def on_ready():
  print('Logged in')
  print('Name : {}'.format(client.user.name))
  print('ID : {}'.format(client.user.id))
  print(discord.__version__)
  print('======== Corp Console ========')

@client.command(pass_context=True)
async def ping(ctx):
    """Pong."""
    await client.say("""Pong""")

@client.command(pass_context=True)
async def info(ctx):
    """Information"""
    await client.say("""Corp Server: https://discord.gg/qDZBRxu If you are banned, we are not going to unban you unless you can actually prove yourself right and that you should be unbanned.""")

@client.command(pass_context=True)
async def developers(ctx):
    """Corp's Developers."""
    await client.say("""MAIN DEVELOPER: ApparenticBubbles
    Developers:Train#1115, Sage#3568""")

@client.command(pass_context=True)
async def apparenticbubbles(ctx):
    """ApparenticBubbles"""
    await client.say("""ApparenticBubbles is Corp's main Developer working 24/7. ApparenticBubbles is hard working proberally right now.""")

@client.command(pass_context=True)
async def sage(ctx):
    """Sage"""
    await client.say("""Sage is one of Corp's Developers. He codes other bots too!""")

client.run('MzAwNDAzODE5MzQ5NTQwODY1.C80yuA.PahB5x8Tc2axyds5sRSvSgXwN70')
