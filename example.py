import bdfdpy as bdfd
from decouple import config

description = '''An example bot to show the usage of bdfdpy'''

token = config('token')

intents = bdfd.discord.Intents.default() 
intents.members = True 

bdfd.bot("e!", description, intents)

 
bdfd.bot_run(token)
bdfd.bot_command("ping", "pong")
