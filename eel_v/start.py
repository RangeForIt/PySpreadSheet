import eel
from web.backend.connect import Connect

eel.init('web')

Connect()

eel.start('html/connect.html', mode=False)