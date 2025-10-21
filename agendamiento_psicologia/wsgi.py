import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agendamiento_psicologia.settings")
application = get_wsgi_application()
