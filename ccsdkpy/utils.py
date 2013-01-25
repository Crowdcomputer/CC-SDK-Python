'''
Created on Jan 25, 2013

@author: stefanotranquillini
'''
from ccsdkpy.auth import CMAuth
from ccsdkpy.exceptions import MethodNotSupported
import requests
import logging
logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger(__name__)




GET= 'GET'
POST='POST'
PUT='PUT'
DELETE='DELETE'

def apiCall(method, url,data=None):    
    if (method == GET):
        return  __apicallGet(url)
    elif (method == POST):
        return __apicallPost(url,data)
    elif (method == GET):
        return __apicallPut(url,data)
    else:
        raise MethodNotSupported
    
def __apicallPut(url,data):
        r=requests.put(url,auth=CMAuth(),  data=data)
        return r
    

def __apicallPost(url,data):
        r=requests.post(url,auth=CMAuth(), data=data)
        return r
    
def __apicallGet(url):
        r=requests.get(url,auth=CMAuth())
        return r
    
def validCall(r):
#    log.debug("status %s " % r.status_code)
#    if r.status_code != (400 and 500):
#        return True
#    return False
    log.warn("TODO")
    return True

def getValue(r,field):
    ret = r.json[field]
    log.debug("%s = %s"%(field,ret))
    return ret

def createData(list):
    data = {}
    for key, val in list:
        data[key]=val
    return data