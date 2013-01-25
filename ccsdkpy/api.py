'''
Created on Jan 25, 2013

@author: stefanotranquillini
'''
from ccsdkpy.utils import apiCall,GET, POST, PUT, createData
import logging

__PREFIX='http://localhost:8000/api/'
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
#process list
def processList():
    url=__PREFIX+'processes/'
    res=apiCall(GET,url)
    log.debug("Process List res %s" % res.text)
    return res
#process create
def processCreate(title, description):
    url=__PREFIX+'processes/'
    data=createData(locals().items())
    res=apiCall(POST,url,data)
    log.debug("Process Create res %s" % res.text)
    return res

def processDetails(pk):
    url=__PREFIX+'processes/pk/'.replace('pk', str(pk))
    res=apiCall(GET,url)
    log.debug("Process Detail res %s" % res.text)
    return res

#process details

#process start

#create task for Process

#task details

#task instances list

#task instance detail

#create user

#assign user to instance