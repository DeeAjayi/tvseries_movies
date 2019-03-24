from tvseries_movies.settings.common import *



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # Once you set DEBUG = FALSE THEN ALLOWED_HOSTS needs to be specified

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', 'localhost'] # Replace value to the host( where you will be hosting the site

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# Remember to change this during production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}



