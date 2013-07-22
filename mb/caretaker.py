# -*- coding: utf-8 -*-
'''
Created on Jul 18, 2013

@author: Carl
'''

from mb.config import urls
from mb.coordinator import *
from web.webapi import HTTPError

class Caretaker(object):
    '''
    整个系统的掌管者
    '''
    _template = None
    
    def __init__(self):
        _template = MBTemplate()
        _template.init()
    
    def start(self):
        self.startWebServer()
            
    def startWebServer(self):
        MBLogger.info('Starting Server ...')
        web.webapi.notfound = noPage
        web.webapi.internalerror = noPage
        web.config.debug = False
        app = web.application(urls, globals())
        app.run()

class _NotFound(HTTPError):
    """`404 Not Found` error."""
    message = "not found1111111"
    def __init__(self, message=None):
        status = '404 Not Found'
        headers = {'Content-Type': 'text/html'}
        HTTPError.__init__(self, status, headers, message or self.message)

def noPage(message=None):
    if message:
        return _NotFound(message)
    else:
        return _NotFound()