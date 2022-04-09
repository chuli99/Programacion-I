from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import FeedbackModel
#Diccionario de prueba
FEEDBACKS = {
    1: {'comment': 'Buen Poema', 'Autor': 'mauri23'},
    2: {'comment': 'I like it', 'Autor': 'lioneldestroyer'},
}

#Recurso Feedback
class Feedback(Resource):
    #Obtener recurso
    def get(self, id):
        feedback = db.session.query(FeedbackModel).get_or_404(id)
        return feedback.to_json()
    #Eliminar recurso
    def delete(self, id):
        feedback = db.session.query(FeedbackModel).get_or_404(id)
        db.session.delete(feedback)
        db.session.commit()
        return '', 204

#Recurso Feedbacks
class Feedbacks(Resource):
    def get(self):
        feedbacks = db.session.query(FeedbackModel).all()
        return jsonify([feedback.to_json_short() for feedback in feedbacks])

    """
            list_feedback = []
            for feedback in feedbacks:
                list_feedback.append(feedback.to_json())
            return jsonify(list_feedback)
    """


    #Insertar recurso
    def post(self):
        #Obtener datos de la solicitud
        feedback = FeedbackModel.from_json(request.get_json())
        db.session.add(feedback)
        db.session.commit()
        return feedback.to_json(), 201
        
