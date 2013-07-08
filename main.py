import web
import mb

class home:
	def GET(self):
		render = web.template.render('templates/', base='layout')
		return render.test()
#		return "Hey, world!!! I am back!!!"

class redirect:
	def GET(self, path):
		web.seeother('/' + path)

if __name__ == "__main__":
	app = web.application(mb.conf.urls, globals())
	app.run()
