# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/c/charlyms/django17.beget.tech/Football')
sys.path.insert(1, '/home/c/charlyms/.local/lib/python3.10/site-packages/django/__init__.py')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Football.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()