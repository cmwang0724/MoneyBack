# -*- coding: utf-8 -*-
'''
Created on Jul 18, 2013

@author: Carl
'''
import web
import mb
from web.webapi import HTTPError
from mb.logger import MBLogger
from mb.config import ERROR_NO_404_STR, ERROR_NO_500_STR

#模板
_Template = None

class Context():
    def init(self):
        global _Template
        _Template  = mb.template.Template()

class Home:
    def GET(self):
        return _Template.render("home")

class Redirect:
    def GET(self, path):
        web.seeother('/' + path)
        
class Pretty(object):
    def handleError(self, message, errno):
        MBLogger.error(message)
        self.handle(errno)
    
    def handle(self, errno):
        web.seeother('/error/' + str(errno))
        
    def page_404(self):
        return _Template.render("page_404")

    def page_500(self):
        return _Template.render("page_500")
    
#以好看的样式处理错误    
_Pretty = Pretty()

class Error:
    '''
    错误处理
    '''
    def __init__(self):
        self._mapping = {
            ERROR_NO_404_STR : lambda : _Pretty.page_404(),
            ERROR_NO_500_STR : lambda : _Pretty.page_500()
        }
    def GET(self, errno):
        return self._mapping[str(errno)]()
        
class _NotFound(HTTPError):
    """`404 Not Found` error."""
    def __init__(self):
        status = '404 Not Found'
        headers = {'Content-Type': 'text/html'}
        HTTPError.__init__(self, status, headers, _Pretty.page_404())
        
class _InternalError(HTTPError):
    """500 Internal Server Error`."""
    def __init__(self):
        status = '500 Internal Server Error'
        headers = {'Content-Type': 'text/html'}
        HTTPError.__init__(self, status, headers, _Pretty.page_500())

def NotFound(message=None):
    """Returns HTTPError with '404 Not Found' error from the active application.
    """
    return _NotFound()

def InternalError(message=None):
    """Returns HTTPError with '500 internal error' error from the active application.
    """
    return _InternalError()