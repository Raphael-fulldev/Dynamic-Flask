from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config) #(Config) is the class name
db = SQLAlchemy(app) #Create DB instance
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

from app import routes, models