from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

Bootstrap(app)

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

from app import routes, models, forms