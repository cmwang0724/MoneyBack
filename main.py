# -*- coding: utf-8 -*-
import web
import mb
from mb.logger import MBLogger

class home:
	def GET(self):
		return mb.template.render("hello", name="Carl")

class redirect:
	def GET(self, path):
		web.seeother('/' + path)

if __name__ == "__main__":
	MBLogger.info('Starting Server ...')
	app = web.application(mb.config.urls, globals())
	app.run()
