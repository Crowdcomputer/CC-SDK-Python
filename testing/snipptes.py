'''
Created on Feb 20, 2013

@author: stefanotranquillini

to test pieces of code
'''
my_id='ea02b01de08ac1848660d80cf0cf8360436d4c68'
app_id='242d9ffac3744ddb8dce43547291314d'

from ccsdkpy import api

a = api.API(my_id,app_id,'http://localhost:8000/')
print a.userGetOrCreate(username='possadsfdsafdfafs',email='palnasdfdssdafffsfdssdnfdsdsfsso@google.com').text
#id = a.getValue(a.createReward(type='CCM',quantity=0.0),'id')
#print a.createTask(pk=2,title='ciao',description='ciao 2',instances_required=2,reward=id).json
#print a.createTask(pk=2,title='ciao',description='ciao 2',instances_required=2,reward=id).json

id = a.getValue(a.createReward(type='CCM',quantity=0.0),'id')
a.createTask(pk=2,title='ciao',description='ciao 2',instances_required=2,reward=id)