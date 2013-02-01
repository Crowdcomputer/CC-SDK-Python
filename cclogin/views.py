# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.conf import settings
import logging

#this function recive back the url
log = logging.getLogger(__name__)
def LoginAPI(request):
    try: 
        f=request.GET['token']
        request.session['token']=f.replace('#_=_','')
        log.debug('fine '+f)

        return redirect('/')
    except Exception:
        data={}
        url_login=settings.CM_LOCATION+"apilogin"
        data['cm_login']=url_login
        log.debug('execption')
        print 'exception'
        return render_to_response('cclogin/login_cc.html', data, context_instance=RequestContext(request))
def LogoutAPI(request):
    try:
        del request.session['token'];
    except KeyError:
        pass
    return redirect('/')



    