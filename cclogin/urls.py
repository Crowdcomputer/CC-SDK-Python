'''
Created on Feb 1, 2013

@author: stefanotranquillini
'''
from django.conf.urls import patterns, url
from cclogin import views
urlpatterns = patterns('',
    url(r'^login/$', views.LoginAPI, name='login-api'),
#    url(r'^campaign/$', views.CampaignCreate, name='campaign')
    
    #url(r'^campaign/$', TemplateView.as_view(template_name="survey/campaign.html"), name='campaign'),
    
    )