from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import UserModel,PoemModel,FeedbackModel
from sqlalchemy import func
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import admin_required

#Recurso usuario
class User(Resource):
    #Obtener recurso si se obtiene un recurso valido. Esta protegida 
    #para cualquier usuario que quiera ingresar con un usuario incorrecto
    @jwt_required()
    def get(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        return user.to_json()
    #Eliminar recurso usuario si verifica que es usuario, y verifica que es Admin
    
    @admin_required
    def delete(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
    
    #Modificar recurso Usuario
    @jwt_required()
    def put(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(user, key, value)
        db.session.add(user)
        db.session.commit()
        return user.to_json, 201

 
#Recurso usuarios
class Users(Resource):
    #Obtener lista de recursos de usuario
    @jwt_required()
    def get(self):
        #valor page por defecto
        page = 1
        per_page = 20
        users = db.session.query(UserModel)
        if request.get_json():
            #traigo todo los items del body de consulta de insomnia
            filters = request.get_json().items()
            #recorremos uno a uno y guardamos en cada iteracion clave valor
            for key,value in filters:
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
                if key == "name":
                    #cadena para que busque nombres similares al indicado, para evitar errores
                    users = users.filter(UserModel.name.like("%"+value+"%"))
                if key == "poems_count":
                    users = users.outerjoin(UserModel.poems).group_by(UserModel.id).having(func.count(PoemModel.id) >= value)  
                if key == "feedbacks_count":
                    users = users.outerjoin(UserModel.feedbacks).group_by(UserModel.id).having(func.count(FeedbackModel.id) >= value)               
                if key == "order_by":
                    #ordena de forma z-a
                    if value == "name[desc]":
                        users = users.order_by(UserModel.name.desc())
                    #ordena de forma a-z
                    if value == "name": 
                        users = users.order_by(UserModel.name)
                    if value == "poems_count[desc]":
                        users = users.outerjoin(UserModel.poems).group_by(UserModel.id).order_by(func.count(PoemModel.id).desc())
                    if value == "poems_count":
                        users = users.outerjoin(UserModel.poems).group_by(UserModel.id).order_by(func.count(PoemModel.id))       
        users = users.paginate(page,per_page,True,20)
        #ya no retornamos una lista de elementos, sino una paginacion
        return jsonify({'users':[user.to_json_short() for user in users.items],
        'total' : users.total,
        'pages' : users.pages,
        'page' : page
        })

    """
            list_user = []
            for user in users:
                list_user.append(user.to_json())
            return jsonify(list_user)
    """

    #Insertar recurso
    def post(self):
        user = UserModel.from_json(request.get_json())
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201

