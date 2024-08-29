"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i_#^n^r&8vuj(!^lsp$b@$e1uku3=5n_&f)#sjm%c9%*iq&h&*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.31.152', '*', '172.25.160.1'] 


# Application definition

INSTALLED_APPS = [
    'rest_framework', 
    'rest_framework_simplejwt',

    'drf_yasg',
    # 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',


    'apps.banner',
    'apps.product',
    'apps.collection',
    'apps.logo',
    'apps.register',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





# JAZZMIN_SETTINGS = {
#     "site_title": "Geeks",  # Заголовок админ-панели
#     "site_header": "Geeks",  # Заголовок на экране входа
#     "site_brand": "Geeks",  # Бренд в верхней части админ-панели
#     "welcome_sign": "Добро пожаловать в Geeks",  # Приветственное сообщение
#     "site_title": "Geeks",  # Заголовок админ-панели
#     "site_header": "Geeks",  # Заголовок на экране входа
#     "site_brand": "Geeks",  # Бренд в верхней части админ-панели
#     "welcome_sign": "Добро пожаловать в Geeks",  # Приветственное сообщение
#     "search_model": ["auth.User", "blog.Post"],  # Модели, доступные для поиска
#     "topmenu_links": [
#         {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
#     ],
#     "show_sidebar": True,
#     "changeform_format": "horizontal_tabs",
#     "header_classes": "navbar-dark bg-dark",  # Темный фон верхней части админ-панели
#     "header_color": "#000000",  # Черный цвет верхней части админ-панели
#     "dark_mode_theme": True,  # Включить темный режим
#     "show_language_chooser": True,  # Включить выбор языка в админ-панели
#     "custom_css": None,  # Путь к пользовательскому CSS-файлу (если нужен)
#     "show_ui_builder": True,  # Показать UI Builder
#     "menu": [
#         {
#             "app": "index",  # Имя вашего приложения Django
#             "name": "Основные параметры",  # Имя модели
#             "icon": "fa fa-cogs",  # Иконка для меню
#             "models": [
#                 {
#                     "name": "Первая модель",  # Имя вашей модели
#                     "icon": "fa fa-cog",  # Иконка для модели
#                     "model": "index.Settings",  # Имя модели в формате "app_label.model_name"
#                 },
#                 # Добавьте другие модели, если необходимо
#             ],
#         },
#         # Добавьте другие приложения и модели, если необходимо
#     ],
    
# }




# Ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'  # URL to jQuery
CKEDITOR_IMAGE_BACKEND = "pillow"  # Путь к пакету Pillow для обработки изображений
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',  # Вы можете настроить свою собственную панель инструментов CKEditor
        'height': 300,
        'width': 800,
    },
}



CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "https://49cd-158-181-248-104.ngrok-free.app",
    "http://localhost:3000",
    "http://192.168.31.152",
    "http://172.25.160.1",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "authorization",
    "content-type",
    "origin",
    "x-csrftoken",
    "x-requested-with",
]

CSRF_TRUSTED_ORIGINS = [
    "https://49cd-158-181-248-104.ngrok-free.app",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://192.168.31.152",
    "http://172.25.160.1",
]

AUTH_USER_MODEL = 'register.User'
