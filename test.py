import bdfdpy as bdfd
from decouple import config

token = config('token')

bdfd.client_run(token)
bdfd.bot_command("e!test", "success")
