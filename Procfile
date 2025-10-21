release: python manage.py migrate && python manage.py createsuperuser --noinput || true
web: gunicorn agendamiento_psicologia.wsgi
