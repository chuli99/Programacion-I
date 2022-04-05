from gettext import gettext
import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from os import path, getenv, mknod
#Directorio de recursos
api = Api()
#import main.resources as resources
db = SQLAlchemy()



def create_app():

	app = Flask(__name__)
	load_dotenv()
	if not path.exists(getenv("DATABASE_PATH")+gettext("DATABASE_NAME")):
		mknod(getenv("DATABASE_PATH")+getenv("DATABASE_NAME"))

	#Para que no se trackeenlas modificaciones que estan pasando en la base de datos
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	#Indica donde tiene que hacer la conexion a la base de datos
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + getenv("DATABASE_PATH") + getenv("DATABASE_NAME")
	db.init_app(app)
	#Cargamos a la API Poems
	api.add_resource(resources.PoemsResource,'/poems')
	#Cargamos a la API Poem
	api.add_resource(resources.PoemResource,'/poem/<id>')
	#Cargamos a la API Users
	api.add_resource(resources.UsersResource,'/users')
	#Cargamos a la API User
	api.add_resource(resources.UserResource,'/user/<id>')
	#Cargamos a la API Feedbacks
	api.add_resource(resources.FeedbacksResource,'/feedbacks')
	#Cargamos a la API Feedback
	api.add_resource(resources.FeedbackResource,'/feedback/<id>')

	#Cargamos la aplicacion en la API de Flask Restful
	api.init_app(app)
	return app

