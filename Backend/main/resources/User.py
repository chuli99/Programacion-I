from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import UserModel


#Recurso usuario
class User(Resource):
    #pagina inicial por defecto
    #page = 1
    #Cantidad de elementos por pagina
    #per_page = 10
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
        #valor page por defecto
        page = 1
        per_page = 5
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
                    users = users.filter(UserModel.name.like("%"+value+"%"))
                
        users = users.paginate(page,per_page,True,20)
        #ya no retornamos una lista de elementos, sino una paginacion
        return jsonify({'users':[user.to_json() for user in users.items],
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

