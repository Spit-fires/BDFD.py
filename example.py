import bdfdpy as bdfd
from decouple import config

description = '''An example bot to show the usage of bdfdpy'''

token = config('token')

intents = bdfd.discord.Intents.default() 
 bdfd.intents.members = True 
 
bot = bdfd.commands.Bot(command_prefix = 'e!', description = description, intents = intents)
 
bdfd.bot_run(token)
bdfd.bot_command("e!ping", "pong")
