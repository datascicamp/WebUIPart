import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2c445f2022'
    ADDRESS_COMP = 'http://45.78.76.192:30600/api/competition/all-competitions'
    # ADDRESS_COMP = 'http://174.137.53.253:30500/api/competition/all-competitions'


