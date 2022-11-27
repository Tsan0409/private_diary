from .settings_common import *

SECRET_KEY = "django-insecure-sv5u%c7xu%tl_*r+577hsdsdj8w_gvpjt@o4s@)c1g5u4+@p9n"

DEBUG = True

ALLOWED_HOSTS = []

LOGGING = {
    'version': 1,  # 1固定
    'disable_existing_loggers': False,

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# メディアファイル
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
