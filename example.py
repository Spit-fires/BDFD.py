import bdfdpy as bdfd
from decouple import config
import discord
from discord.ext import commands

description = '''An example bot to show the usage of bdfdpy'''

token = config('token')
prefix = "e!"
bdfd.bot(prefix)


bdfd.bot_run(token)
bdfd.bot_command("test", "hi im a test")
bdfd.client_command("e!ping", "pong")
