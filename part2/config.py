class config:
    """Base configuration."""
    SECRET_KEY = 'dev'
    DEBUG = False

class developmentConfing(config):
    """Development configuration."""
    DEBUG = True

class productionConfing(config):
    """Production configuration."""
    DEBUG = False