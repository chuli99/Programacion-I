from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import PoemModel

#Diccionario de prueba
POEMS = {
    1: {'name': 'Por mil noches', 'Autor': 'mauri23'},
    2: {'name': 'El secreto de sus ojos', 'Autor': 'lioneldestroyer'},
}


#Recurso Poem
class Poem(Resource):
    #Obtener recurso
    def get(self, id):
        poem = db.session.query(PoemModel).get_or_404(id)
        return poem
    #Eliminar recurso
    def delete(self, id):
        #Verificar que exista un Poema con ese Id en diccionario
        poem = db.session.query(PoemModel).get_or_404(id)
        db.session.delete(poem)
        db.session.commit()
        return '', 204

    #Modificar recurso
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
    #Obtener lista de recursos
    def get(self):
        poems = db.session.query(PoemModel).all()
        return jsonify([poem.to_json_short() for poem in poems])

    """
            list_poem = []
            for poem in poems:
                list_poem.append(poem.to_json())
            return jsonify(list_poem)
    """


    #Insertar recurso
    def post(self):
        #Obtener datos de la solicitud
        poem = PoemModel.from_json(request.get_json())
        db.session.add(poem)
        db.session.commit()
        return poem.to_json(), 201
        
