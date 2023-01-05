import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gerenciador.settings')

application = get_wsgi_application()


# # If using WhiteNoise:
# from whitenoise import WhiteNoise
# application = WhiteNoise(get_wsgi_application())