from flask_restful import Resource
from flask import request

#Diccionario de prueba
FEEDBACKS = {
    1: {'comment': 'Buen Poema', 'Autor': 'mauri23'},
    2: {'comment': 'I like it', 'Autor': 'lioneldestroyer'},
}

#Recurso Feedback
class Feedback(Resource):
    #Obtener recurso
    def get(self, id):
        #Verificar que exista Feedback con ese Id en diccionario
        if int(id) in FEEDBACKS:
            #Devolver feedback correspondiente
            return FEEDBACKS[int(id)]
        #Devolver error 404 en caso que no exista
        return '', 404
    #Eliminar recurso
    def delete(self, id):
        #Verificar que exista un Poema con ese Id en diccionario
        if int(id) in FEEDBACKS:
            #Eliminar feedback del diccionario
            del FEEDBACKS[int(id)]
            return '', 204
        return '', 404
    

#Recurso Feedbacks
class Feedbacks(Resource):
    #Obtener lista de recursos
    def get(self):
        return FEEDBACKS
    #Insertar recurso
    def post(self):
        #Obtener datos de la solicitud
        feedback = request.get_json()
        id = int(max(FEEDBACKS.keys())) + 1
        FEEDBACKS[id] = feedback
        return FEEDBACKS[id], 201
