from tvseries_movies.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lsuf%evvg74c#6$=9e0bgvm(#^e6uh658j(yxo#w&i!8=b3^)i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}