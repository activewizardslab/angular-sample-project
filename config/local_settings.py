# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd=xfpo$-0a1)zhxi7n^65%u-5&idiwrs&s%&@&w=#anp_0_4qv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'logs': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'awo174_logs',
        'USER': 'root',
        'PASSWORD': '12344321',
    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'awo174_users',
        'USER': 'root',
        'PASSWORD': '12344321',
    },
}
