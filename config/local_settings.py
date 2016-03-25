# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd=xfpo$-0a1)zhxi7n^65%u-5&idiwrs&s%&@&w=#anp_0_4qv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'awo174_users',
        'USER': 'root',
        'PASSWORD': '12344321',
    },
    'logs': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'awo174_logs',
        'USER': 'root',
        'PASSWORD': '12344321',
    },
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'awo42test@gmail.com'
EMAIL_HOST_PASSWORD = 'knuvimdpuoumzqrz'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
