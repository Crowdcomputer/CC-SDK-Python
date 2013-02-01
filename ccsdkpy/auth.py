'''
Created on Jan 25, 2013

@author: stefanotranquillini
'''

from requests.auth import AuthBase
from django.conf import settings

class CMAuth(AuthBase,):
    def __init__(self, token,apptoken):
        # setup any auth-related data here
        self.token = token 
        self.app_token=apptoken

    def __call__(self, r):
        # modify and return the request
        r.headers['Authorization'] = 'Token '+ self.token
        r.headers['APP_ID'] = self.app_token
        return r
