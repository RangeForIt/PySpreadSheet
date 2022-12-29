from web.backend.connect import Connect

import eel

eel.init('web')

Connect()

eel.start('html/connect.html', mode=False)