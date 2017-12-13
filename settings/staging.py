from base import *
import dj_database_url


DEBUG = False

#DATABASES = {
 #  'default': dj_database_url.config('CLEARDB_DATABASE_URL')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_1URLx914YWI0EgBoUgFr3COE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_k5mTHdMFNHuD5NmgTTmsjFuk')


SITE_URL = 'https://fusion-fitness.herokuapp.com'
ALLOWED_HOSTS.append('fusion-fitness.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

