'''
Created on Jan 25, 2013

@author: stefanotranquillini
'''

from requests.auth import AuthBase

class CMAuth(AuthBase,):
    def __init__(self, token):
        # setup any auth-related data here
        self.token = token 

    def __call__(self, r):
        # modify and return the request
        r.headers['Authorization'] = 'Token '+ self.token
        return r
