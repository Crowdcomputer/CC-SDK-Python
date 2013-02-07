'''
Created on Oct 9, 2012

@author: stefanotranquillini
'''
def global_vars(request):
    try:
        request.session['token']
        logged_in = True
    except Exception:
        logged_in = False
    return {
        'logged_in': logged_in
    }
