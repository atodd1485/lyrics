import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'  # Used for session and CSRF protection
    DEBUG = True  # Turn off debug mode for production
    TESTING = False  # Testing mode off by default
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class DevelopmentConfig(Config):
    DEBUG = True  # Enable debug mode


class ProductionConfig(Config):
    DEBUG = False  # Ensure debug mode is off in production


