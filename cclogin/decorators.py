import logging
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import redirect

log = logging.getLogger(__name__)


def isLoggedInCC(function):
    def wrap(request, *args, **kwargs):
                #this check the session if userid key exist, if not it will redirect to login page
        if 'token' not in request.session.keys():
            log.debug("redirect %s",reverse('login-api'))
            request.session['url_requ']=request.build_absolute_uri()
            return redirect(reverse('login-api'))
        return function(request, *args, **kwargs)
    
    wrap.__doc__=function.__doc__
    wrap.__name__=function.__name__
    return wrap