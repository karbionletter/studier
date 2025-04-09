"""
WSGI config for studier_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

sys.path.insert(0, 'C:/Env/localassets')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'localassets.settings')

application = get_wsgi_application()
