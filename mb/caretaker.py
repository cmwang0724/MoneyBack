# -*- coding: utf-8 -*-
'''
Created on Jul 18, 2013

@author: Carl
'''

from mb.config import urls
from mb.coordinator import *

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
        app = web.application(urls, globals())
        web.config.debug = False
        app.run()