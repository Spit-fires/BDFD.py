import bdfdpy as bdfd
from decouple import config

token = config('token')

bdfd.client.run(token)
bdfd.bot.command($, test)