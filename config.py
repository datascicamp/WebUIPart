import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2c445f2022'
    ADDRESS_COMP = 'http://45.78.76.192:30600/api/competition/all-competitions'
    # ADDRESS_COMP = 'http://174.137.53.253:30500/api/competition/all-competitions'

    # for account info handling api
    ACCOUNT_SERVICE_IP = '127.0.0.1'
    ACCOUNT_SERVICE_PORT = '4998'
    ACCOUNT_SERVICE_URL = ACCOUNT_SERVICE_IP + ':' + ACCOUNT_SERVICE_PORT

    # for mail sending support api
    MAIL_SENDING_SERVICE_IP = '127.0.0.1'
    MAIL_SENDING_SERVICE_PORT = '4999'
    MAIL_SENDING_SERVICE_URL = MAIL_SENDING_SERVICE_IP + ':' + MAIL_SENDING_SERVICE_PORT


