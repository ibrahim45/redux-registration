# redux-registration


Redux Registration

ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window; you may, of course, use a different value.


# Email Setup(Gmail)
EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = '********@gmail.com'

EMAIL_HOST_PASSWORD = ''********'

EMAIL_PORT = 587


# django.contrib.auth should be next to registration
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'registration',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]


# registration.backends.default.urls will replace django inbuilt urls /accounts and activation email will be sent
# registration.backends.simple.urls will replace django inbuilt urls /accounts but no activation email will be sent
    url(r'^accounts/',
        include('registration.backends.default.urls')),
