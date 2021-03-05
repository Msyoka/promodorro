import os

class Config:
    SECRET_KEY=os.environ.get(SECRET_KEY)
    SQLALCHEMY_DATABASE_URI="Postgresql+Psycopg2//Access:KAROL@localhost/promodoro
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG=True
config_options={
    'development':DevConfig'
    'production':ProdConfig
}   