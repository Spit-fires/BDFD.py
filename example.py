import bdfdpy as bdfd
from decouple import config

token = config('token')

bdfd.bot_run(token)
bdfd.bot_command("e!ping", "pong")
