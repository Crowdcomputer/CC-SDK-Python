'''
Created on Jan 25, 2013

@author: stefanotranquillini
'''
import logging
from exceptions import TokenNotDefinedException, MissingConfiguration, MethodNotSupported
from auth import CMAuth
import requests
import logging
from django.conf import settings
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
    __api_token=''
    
    def __init__(self,request):
#    def register(self,t):
#        d = shelve.open(__FILENAME)
#        d['token'] = t 
        log.debug("Location %s " , settings.CM_LOCATION)
        self.__token=request.session['token'];
        self.__url=settings.CM_LOCATION
        self.__api_token=settings.APP_ID_TOKEN

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
        url=self.__url+'api/processes/pk/'.replace('pk', str(pars['pk']))
        res=self.apiCall(GET,url)
        log.debug("Process Detail res %s" % res.text)
        return res

    def createTask(self, **pars):
        url=self.__url+'api/processes/pk/task/'.replace('pk', str(pars['pk']))
        res=self.apiCall(POST,url,pars)
        log.debug("Task Create res %s" % res.text)
        return res
    
    def startStopProcess(self, **pars):
        url=self.__url+"api/processes/pk/startstop/".replace('pk', str(pars['pk']))
        res=self.apiCall(POST,url,pars)
        log.debug("StartStop res %s" % res.text)
        return res
    
    def taskInstances(self, **pars):
        url=self.__url+"api/task/pk/taskinstances/".replace('pk', str(pars['pk']))
        res=self.apiCall(GET,url)
        log.debug("taskInstance res %s" % res.text)
        return res
    
    def taskInstanceDetail(self, **pars):
        url=self.__url+"api/taskinstance/pk/".replace('pk', str(pars['pk']))
        res=self.apiCall(GET,url)
        log.debug("taskInstance res %s" % res.text)
        return res
    
    def userGetOrCreate(self, **pars):
        url=self.__url+"api/users/"
        res=self.apiCall(POST,url,pars)
        log.debug("User res %s" % res.text)
        return res
    
    def updateInsance(self, **pars):
        url=self.__url+"api/taskinstance/pk/".replace('pk', str(pars['pk']))
        log.debug('updaate data %s' , pars['data'])
        res=self.apiCall(PUT,url,pars['data'])
        log.debug("taskInstanceUpdate res %s" % res.text)
        return res
        
    def whoami(self):
        url=self.__url+"api/users/me/"
        res=self.apiCall(GET,url)
        log.debug("me res %s" % res.text)
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
            res = self.__apicallGet(url)
        elif (method == POST):
            res= self.__apicallPost(url,data)
        elif (method == PUT):
            res= self.__apicallPut(url,data)
        else:
            raise MethodNotSupported
        self.validCall(res)
        return res    

        
    def __apicallPut(self,url,data):
            r=requests.put(url,auth=CMAuth(self.__getToken(),self.__api_token),  data=data)
            return r
        
    
    def __apicallPost(self,url,data):
            r=requests.post(url,auth=CMAuth(self.__getToken(),self.__api_token), data=data)
            return r
        
    def __apicallGet(self,url):
            r=requests.get(url,auth=CMAuth(self.__getToken(),self.__api_token))
            return r
        
    def validCall(self,r):
        log.warn("TODO")
        if r.status_code == (500 or 400):
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