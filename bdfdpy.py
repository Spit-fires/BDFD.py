import math
import time
import discord.py
import logging
from discord.ext import commands

# logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# discord.py stuff

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

# functions

def fetch(pkg):
  import pkg
  
def log(text):
  print(text)
  
def bot_command(trigger, response):
  @bot.command()
  async def trigger(ctx, *args):
    await ctx.send(response)
          
def bot_token(token):
  client.run(token)

