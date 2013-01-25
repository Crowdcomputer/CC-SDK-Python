'''
Created on Jan 25, 2013

@author: stefanotranquillini
'''
import unittest

from ccsdkpy import auth, api, utils
import logging
import time 
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class Auth(unittest.TestCase):

    def testSetToken(self):
        self.assertTrue(auth.register('1234'), 'registration went wrong')

    def testToken(self):
        self.assertEqual(auth.token(), '1234', 'token stored is wrong')

class API(unittest.TestCase):

        
    def setUp(self):
        auth.register('91a2c9d55ecac465eb16bb481086dbc9dccc1ef9')
        self.pk=1
        
    def testProcessList(self):
        res = api.processList()
        self.assertEqual(res.status_code, 200, 'Process List failed, status code is %s ' % res.status_code)
        log.debug(res.json)
        
    def testProcessCreate(self):
        t = str(time.time())
        res = api.processCreate('title-'+t,'desc-'+t)
        self.assertEqual(res.status_code, 201, 'Process Creation failed, status code is %s ' % res.status_code)
        log.debug(res.json)
        self.pk=utils.getValue(res,'pk')
        self.assertEqual(self.pk, utils.getValue(res,'pk'), res.json)
        res = api.processDetails(self.pk)
        self.assertEqual(res.status_code, 200, 'Process Detail failed, status code is %s ' % res.status_code)
#        self.assertEqual(res.json['pk'], self.pk, 'Process Detail failed, pk is %s ' % res.json['pk'])
        
        

        
if __name__ == "__main__":
    unittest.main()
    
    