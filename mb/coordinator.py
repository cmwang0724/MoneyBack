# -*- coding: utf-8 -*-
'''
Created on Jul 18, 2013

@author: Carl
'''
import web
import mb
from mb.logger import MBLogger
from mb.config import ERROR_NO_404_STR, ERROR_NO_500_STR

class MBTemplate():
    def init(self):
        global _Template
        _Template  = mb.template.Template()

class Home:
    def GET(self):
        return _Template.render("home")

class Redirect:
    def GET(self, path):
        web.seeother('/' + path)
        
class Error:
    '''
    错误映射
    '''
    _mapping = {
        ERROR_NO_404_STR : lambda : page_404(),
        ERROR_NO_500_STR : lambda : page_500()
    }
    def GET(self, errno):
        return self._mapping[str(errno)]()
    
class Pretty(object):
    def handle(self, message, errno):
        MBLogger.error(message)
        self.handleError(errno)
    
    def handleError(self, errno):
        web.seeother('/error/' + str(errno))
        
def page_404():
    return _Template.render("page_404")

def page_500():
    return _Template.render("page_500")

