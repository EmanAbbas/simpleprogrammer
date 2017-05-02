from .settings import *



SECRET_KEY='svbdx!_y@@726g9*!d1(3$17l_xg)3q^kv)*8#x!aa1529=x_+'

ALLOWED_HOSTS=[]

DEBUG=True
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}