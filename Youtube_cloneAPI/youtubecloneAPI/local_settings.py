# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s18ouq!eiau7r^wh2&ovmedtar_o$+txicqm3u7dbp729fg=2c'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone_database',
        'USER': 'root',
        'PASSWORD': 'Diablaselena666#',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}