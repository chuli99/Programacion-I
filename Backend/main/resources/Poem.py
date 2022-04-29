from datetime import date
from flask_restful import Resource
from flask import jsonify, request
from flask import request
from main.resources.Feedback import Feedbacks
from .. import db
from main.models import PoemModel, UserModel, FeedbackModel
from sqlalchemy import func


#Recurso Poem
class Poem(Resource):
    #Obtener recurso
    def get(self, id):
        poem = db.session.query(PoemModel).get_or_404(id)
        return poem.to_json()

    #Eliminar recurso poema
    def delete(self, id):
        poem = db.session.query(PoemModel).get_or_404(id)
        db.session.delete(poem)
        db.session.commit()
        return '', 204

    #Modificar recurso Poema
    def put(self, id):
        
        poem = db.session.query(PoemModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(poem, key, value)
        db.session.add(poem)
        db.session.commit()
        return poem.to__json, 201


#Recurso Poemas
class Poems(Resource):
    #Obtener lista de recursos de poemas
    def get(self):
        page = 1
        per_page = 10
        poems = db.session.query(PoemModel)
        users = db.session.query(UserModel)
        feedbacks = db.session.query(FeedbackModel)
        if request.get_json():
            #traigo todo los items del body de consulta de insomnia
            filters = request.get_json().items()
            #recorremos uno a uno y guardamos en cada iteracion clave valor
            for key,value in filters:
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
                #filtrado por usuario
                if key == "name":
                    #cadena para que busque nombres similares al indicado, para evitar errores
                    poems = users.filter(UserModel.name.like("%"+value+"%"))
                if key == "qualification":
                    poems = feedbacks.filter(FeedbackModel.qualification == value)
                if key == "feedbacks_count":
                    poems = poems.outerjoin(PoemModel.feedbacks).group_by(PoemModel.id).having(func.count(FeedbackModel.id) >= value)
                if key == "title":
                    poems = poems.filter(PoemModel.title.like("%"+value+"%")) 
                if key == "date":
                    poems = poems.filter(PoemModel.datePoem == value) 
                if key == "order_by":
                    if value == "title[desc]":
                        poems = poems.order_by(PoemModel.title.desc())
                    if value == "title":
                        poems = poems.order_by(PoemModel.title)
                    if value == "qualifications[desc]":
                        poems = feedbacks.order_by(FeedbackModel.qualification.desc())
                    if value == "qualifications":
                        poems = feedbacks.order_by(FeedbackModel.qualification)
                    if value == "date[desc]":
                        poems = poems.order_by(PoemModel.datePoem.desc())
                    if value == "date":
                        poems = poems.order_by(PoemModel.datePoem)
    
        poems = poems.paginate(page,per_page,True,20)
        return jsonify({'poems':[poem.to_json_short() for poem in poems.items],
        'total' : poems.total,
        'pages' : poems.pages,
        'page' : page
        })

    """
            list_poem = []
            for poem in poems:
                list_poem.append(poem.to_json())
            return jsonify(list_poem)
    """

    
    #Insertar recurso
    def post(self):
        poem = PoemModel.from_json(request.get_json())
        db.session.add(poem)
        db.session.commit()
        return poem.to_json(), 201

