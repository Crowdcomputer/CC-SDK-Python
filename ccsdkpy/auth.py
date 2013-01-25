'''
Created on Jan 25, 2013

@author: stefanotranquillini
'''

import shelve
from requests.auth import AuthBase
from ccsdkpy.exceptions import TokenNotDefinedException
__FILENAME='token'

    
def register(t):
    d = shelve.open(__FILENAME)
    d['token'] = t 
    return True
           
def token():
    d = shelve.open(__FILENAME) 
    token= d['token']
    if not token:
        raise TokenNotDefinedException
    return token


class CMAuth(AuthBase):
    def __init__(self):
        # setup any auth-related data here
        self.token = token()

    def __call__(self, r):
        # modify and return the request
        r.headers['Authorization'] = 'Token '+ self.token
        return r
