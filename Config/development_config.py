

class DevelopmentConfig:
    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Server
    SERVER_NAME = 'api.developer.xeosmarthome.com'
