'''
Created on Feb 11, 2013

@author: stefanotranquillini
'''

from ccsdkpy import api
def testAPI():
    ap=api.API('05a0c48244d366b451b3344da44185daa4c2cfbc','87b0223180da43d885bfa11055f13d87')
    api.userGetOrCreate(username='qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjkl',email='ciao@gmail.com')
    print 'fine'
    
if __name__ == '__main__':
    testAPI()