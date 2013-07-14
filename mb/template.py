'''
Created on Jul 11, 2013

@author: Carl
'''
import os
from jinja2 import Environment,FileSystemLoader,TemplateNotFound
from mb.logger import MBLogger

def render(templateName, **context):
    extensions = context.pop('extensions', [])
    globalVars = context.pop('globals', {})
    
    templatePath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
    jinjaEnv = Environment(
            loader=FileSystemLoader(templatePath),
            extensions=extensions,
            )
    jinjaEnv.globals.update(globalVars)
    try:
        return jinjaEnv.get_template(templateName + ".html").render(context)
    except TemplateNotFound:
        MBLogger.error("Cannot find the template[" + templateName + "] in " + templatePath)
        return "Cannot find the template."
    except:
        errorInfo = os.sys.exc_info()
        MBLogger.error("Error '%s' happened on line %d\n" % (errorInfo[0], errorInfo[2].tb_lineno))
        return "Error occurred while rendering the template."