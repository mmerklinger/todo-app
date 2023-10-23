from datetime import timedelta
from os.path import exists

from dotenv import load_dotenv
from flask.config import Config


class DefaultConfig(object):
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = None
    TRAP_HTTP_EXCEPTIONS = False
    TRAP_BAD_REQUEST_ERRORS = None
    SECRET_KEY = None
    SESSION_COOKIE_NAME = "session"
    SESSION_COOKIE_DOMAIN = None
    SESSION_COOKIE_PATH = None
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_SAMESITE = None
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)
    SESSION_REFRESH_EACH_REQUEST = True
    USE_X_SENDFILE = False
    SEND_FILE_MAX_AGE_DEFAULT = None
    SERVER_NAME = None
    APPLICATION_ROOT = "/"
    PREFERRED_URL_SCHEME = "http"
    MAX_CONTENT_LENGTH = None
    TEMPLATES_AUTO_RELOAD = None
    EXPLAIN_TEMPLATE_LOADING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"


def create_config(root_path: str) -> Config:
    config = Config(root_path)
    config.from_object(DefaultConfig())
    load_dotenv()
    config.from_prefixed_env()
    return config
