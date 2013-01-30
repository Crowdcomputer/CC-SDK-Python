'''
Created on Jan 25, 2013

@author: stefanotranquillini
'''
import logging
from ccsdkpy.exceptions import TokenNotDefinedException, MissingConfiguration
from ccsdkpy.auth import CMAuth
from ccsdkpy.exceptions import MethodNotSupported
import requests
import logging
#logging.basicConfig(level=logging.DEBUG)
#
log = logging.getLogger(__name__)



GET= 'GET'
POST='POST'
PUT='PUT'
DELETE='DELETE'
#logging.basicConfig(level=logging.DEBUG)
#log = logging.getLogger(__name__)

class API():
    __token = ''
    __url = ''
    
    def __init__(self, t, location):
#    def register(self,t):
#        d = shelve.open(__FILENAME)
#        d['token'] = t 
        self.__token=t;
        self.__url=location

    def __module_exists(self,module_name):
        try:
            __import__(module_name)
        except ImportError:
            return False
        else:
            return True
           
    def __getToken(self):
#        d = shelve.open(__FILENAME) 
#        token= d['token']
        token = self.__token
        if not token:
            raise TokenNotDefinedException
        return token
    
    
    #process list
    def processList(self):
        url=self.__url+'api/processes/'
        res=self.apiCall(GET,url)
        log.debug("Process List res %s" % res.text)
        return res
    #process create
    def processCreate(self, **pars):
        url=self.__url+'api/processes/'
        res=self.apiCall(POST,url,pars)
        log.debug("Process Create res %s" % res.text)
        return res
    
    def processDetails(self, **pars):
        url=self.__url+'api/processes/pk/'.replace('pk', pars['pk'])
        res=self.apiCall(GET,url)
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

    def apiCall(self,method, url,data=None):   
        log.debug('url %s',url)
        log.debug('data %s', data) 
        if (method == GET):
            return  self.__apicallGet(url)
        elif (method == POST):
            return self.__apicallPost(url,data)
        elif (method == GET):
            return self.__apicallPut(url,data)
        else:
            raise MethodNotSupported
        
    def __apicallPut(self,url,data):
            r=requests.put(url,auth=CMAuth(self.__getToken()),  data=data)
            return r
        
    
    def __apicallPost(self,url,data):
            r=requests.post(url,auth=CMAuth(self.__getToken()), data=data)
            return r
        
    def __apicallGet(self,url):
            r=requests.get(url,auth=CMAuth(self.__getToken()))
            return r
        
    def validCall(self,r):
        log.warn("TODO")
        if r.status_code == 500 or 400:
            log.error("ERROR response : %s ", r.text)
            return False
        return True
        #    log.debug("status %s " % r.status_code)
    #    if r.status_code != (400 and 500):
    #        return True
    #    return False
    
    def getValue(self,r,field):
        ret = r.json[field]
        log.debug("%s = %s"%(field, ret))
        return ret
    
#    def __createData(self, *l):
##        log.debug("list" + list)
#        print l
#        data = {}
#        for key, val in l:
#            data[key]=val
#        return data