from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///local.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class GithubCIConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    DEBUG = True

class DevelopmentConfig(Config):
    # Using environment variables for PostgreSQL DB connection
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',  # This is commonly used for PostgreSQL URLs in hosting platforms
        'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
            dbuser=os.getenv('DBUSER', 'default_user'),
            dbpass=os.getenv('DBPASS', 'default_pass'),
            dbhost=os.getenv('DBHOST', 'localhost'),
            dbname=os.getenv('DBNAME', 'my_database')
        )
    )
    DEBUG = True

class ProductionConfig(Config):
    # Similar to development, but without DEBUG and for production
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
            dbuser=os.getenv('DBUSER', 'default_user'),
            dbpass=os.getenv('DBPASS', 'default_pass'),
            dbhost=os.getenv('DBHOST', 'localhost'),
            dbname=os.getenv('DBNAME', 'my_production_database')
        )
    )
    DEBUG = False
