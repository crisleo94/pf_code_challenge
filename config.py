import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER= os.getenv('POSTGRES_USERNAME')
POSTGRES_PASS= os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DATABASE')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = F'postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@localhost:{POSTGRES_PORT}/{POSTGRES_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig
}