'''
Created on Jul 18, 2013

@author: Carl
'''
import web
import template

class home:
    def GET(self):
        return template.render("hello", name="Carl")

class redirect:
    def GET(self, path):
        web.seeother('/' + path)