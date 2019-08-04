import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2c445f2022'

    DB_SOURCE_IP = '23.106.158.242'
    DB_SOURCE_PORT = '30070'


