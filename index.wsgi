import sae
from adp import wsgi
import os,sys
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))
import django.core.handlers.wsgi
#os.environ['DJANGO_SETTINGS_MODULE'] = 'adp.settings'
application = sae.create_wsgi_app(wsgi.application)

