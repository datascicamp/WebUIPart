import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2c445f2022'

    # Identifiers when generating CAPTCHA
    IDENTIFIERS = 'ABCDEFGHIJKLMNPQRSTUVWXYZ12345789'

    # for account info handling api
    ACCOUNT_SERVICE_IP = '127.0.0.1'
    ACCOUNT_SERVICE_PORT = '4998'
    ACCOUNT_SERVICE_URL = ACCOUNT_SERVICE_IP + ':' + ACCOUNT_SERVICE_PORT

    # for mail sending support api
    MAIL_SENDING_SERVICE_IP = '127.0.0.1'
    MAIL_SENDING_SERVICE_PORT = '4999'
    MAIL_SENDING_SERVICE_URL = MAIL_SENDING_SERVICE_IP + ':' + MAIL_SENDING_SERVICE_PORT

    # for competition supporting api
    COMPETITION_SERVICE_IP = '45.78.76.192'
    COMPETITION_SERVICE_PORT = '30600'
    COMPETITION_SERVICE_URL = COMPETITION_SERVICE_IP + ':' + COMPETITION_SERVICE_PORT

    # for captcha supporting api
    CAPTCHA_SERVICE_IP = '45.78.76.192'
    CAPTCHA_SERVICE_PORT = '30601'
    CAPTCHA_SERVICE_URL = CAPTCHA_SERVICE_IP + ':' + CAPTCHA_SERVICE_PORT
