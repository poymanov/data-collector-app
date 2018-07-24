import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	DEBUG = True if os.environ.get('DEBUG') == '1' else False
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = os.environ.get('MAIL_PORT') or 25
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')	
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	MAIL_FROM = os.environ.get('MAIL_FROM')