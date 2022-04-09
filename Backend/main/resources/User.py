from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import UserModel


#Recurso usuario
class User(Resource):
    #Obtener recurso
    def get(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        return user.to_json()
    #Eliminar recurso usuario
    def delete(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
    #Modificar recurso Usuario
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
    def get(self):
        users = db.session.query(UserModel).all()
        return jsonify([user.to_json_short() for user in users])

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

