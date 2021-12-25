import os
from flask import Flask 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_NAME = 'local.db'


def create_app():
	"""Create and return flask application."""
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'random secure key'

	from .views import views 

	app.register_blueprint(views, url_prefix='/')

	from .models import Song 

	create_db()

	return app


def get_current_dir():
	"""Return current path direction."""
	return os.path.dirname(os.path.realpath(__file__))


def get_connection_string():
	"""Return string to initialize database."""
	return "sqlite:///" + os.path.join(get_current_dir(), DB_NAME)


engine = create_engine(get_connection_string(), echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


def create_db():
	"""Create database in case it doesn't exist."""
	if not os.path.exists(os.path.join(get_current_dir(), DB_NAME)):
		Base.metadata.create_all(engine)
