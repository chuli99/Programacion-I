import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from os impor path
#Directorio de recursos
import main.resources as resources

api = Api()

def create_app():

	app = Flask(__name__)
	load_dotenv()
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

