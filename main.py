# -*- coding: utf-8 -*-

from mb.config import urls
from mb.controller import *
from mb.carekeeper import CareKeeper

_careKeeper = CareKeeper()

if __name__ == "__main__":
	_careKeeper.start()
	app = web.application(urls, globals())
	app.run()
