from flask_restful import Resource
from flask import request

#Diccionario de prueba
USERS = {
    1: {'username': 'mauri23', 'email': 'mauricio23@gmail.com'},
    2: {'username': 'lioneldestroyer', 'email': 'lio_killer@gmail.com'},
}
 
#Recurso usuario
class User(Resource):
    #Obtener recurso
    def get(self, id):
        #Verificar que exista un Usuario con ese Id en diccionario
        if int(id) in USERS:
            #Devolver usuario correspondiente
            return USERS[int(id)]
        #Devolver error 404 en caso que no exista
        return '', 404
    #Eliminar recurso
    def delete(self, id):
        #Verificar que exista un Usuario con ese Id en diccionario
        if int(id) in USERS:
            #Eliminar usuario del diccionario
            del USERS[int(id)]
            return '', 204
        return '', 404
    #Modificar recurso
    def put(self, id):
        if int(id) in USERS:
            user = USERS[int(id)]
            #Obtengo los datos de la solicitud
            data = request.get_json()
            user.update(data)
            return user, 201
        return '', 404
 
#Recurso usuarios
class Users(Resource):
    #Obtener lista de recursos
    def get(self):
        return USERS
    #Insertar recurso
    def post(self):
        #Obtener datos de la solicitud
        user = request.get_json()
        id = int(max(USERS.keys())) + 1
        USERS[id] = user
        return USERS[id], 201
