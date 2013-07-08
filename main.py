import web

urls= (
	'/', 'home',
	'/(.*)/', 'redirect'
)

class home:
	def GET(self):
		return "Hey, world!!!"

class redirect:
	def GET(self, path):
		web.seeother('/' + path)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
