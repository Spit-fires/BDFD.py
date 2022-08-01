import bdfd
from decouple import config
import discord
from discord.ext import commands


token = config('token')


# starting the bot
bdfd.bot_run(token)

# command using new command register
bdfd.bot_command("test", "hi im a test")
# command using old command register
bdfd.client_command("e!ping", "pong")
