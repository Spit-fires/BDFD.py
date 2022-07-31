import math
import time
import discord
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

# ping command ()

@bot.command()
async def ping(ctx, *args):
  await ctx.send("pong!")
  
# functions

def fetch(pkg):
  import pkg
  
def log(text):
  print(text)
  
def bot_command(trigger, response):
  @bot.command()
  async def trigger(ctx, *args):
    await ctx.send(response)
          
def bot_run(token):
  client.run(token)

def onlyif(condition, error):
  if condition == false:
    return error 
    
def client_command(trigger, response):
  @client.event
  async def on_message(message):
      if message.author == client.user:
          return
  
      if message.content.startswith(trigger):
          await message.channel.send(response)
          
