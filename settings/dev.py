from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
SITE_URL = 'http://127.0.0.1:8000'
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_1URLx914YWI0EgBoUgFr3COE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_k5mTHdMFNHuD5NmgTTmsjFuk')