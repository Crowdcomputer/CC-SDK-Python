'''
Created on Jan 25, 2013

@author: stefanotranquillini
'''


class TokenNotDefinedException(Exception):
    Message='Token is not defined, set it using "register"'
    
class MethodNotSupported(Exception):
    Message='The method is not supported'
    
class MissingConfiguration(Exception):
    Message='Parameter is missing in the configuration'