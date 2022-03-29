from flask_restful import Resource
from flask import request

#Diccionario de prueba
POEMS = {
    1: {'firstname': 'Pedro', 'lastname': 'Marco'},
    2: {'firstname': 'María', 'lastname': 'Sosa'},
}

#Recurso Profesor
class Poem(Resource):
    #Obtener recurso
    def get(self, id):
        #Verificar que exista un Profesor con ese Id en diccionario
        if int(id) in POEMS:
            #Devolver professor correspondiente
            return POEMS[int(id)]
        #Devolver error 404 en caso que no exista
        return '', 404
    #Eliminar recurso
    def delete(self, id):
        #Verificar que exista un Profesor con ese Id en diccionario
        if int(id) in POEMS:
            #Eliminar professor del diccionario
            del POEMS[int(id)]
            return '', 204
        return '', 404
    #Modificar recurso
    def put(self, id):
        if int(id) in POEMS:
            poem = POEMS[int(id)]
            #Obtengo los datos de la solicitud
            data = request.get_json()
            poem.update(data)
            return poem, 201
        return '', 404

#Recurso Profesores
class Professors(Resource):
    #Obtener lista de recursos
    def get(self):
        return POEMS
    #Insertar recurso
    def post(self):
        #Obtener datos de la solicitud
        poem = request.get_json()
        id = int(max(POEMS.keys())) + 1
        POEMS[id] = poem
        return POEMS[id], 201
