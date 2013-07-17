# -*- coding: utf-8 -*-

from mb.logger import MBLogger
from mb.config import urls
from mb.controller import *

if __name__ == "__main__":
	MBLogger.info('Starting Server ...')
	app = web.application(urls, globals())
	app.run()
