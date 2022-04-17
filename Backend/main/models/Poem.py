from .. import db
from datetime import datetime


class Poem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.String(500), nullable = False)
    datePoem = db.Column(db.DateTime,nullable = False, default = datetime.now() )
    userId = db.Column(db.Integer,db.ForeignKey('user.id'), nullable = False)
    #Relacionamos en back_populates a poems, por la relacion de un usuario a muchos poemas
    user = db.relationship('User',back_populates = "poems", uselist = False,single_parent = True)
    feedbacks = db.relationship('Feedback',back_populates = 'poem', cascade = 'all, delete-orphan')


    def __repr__(self):
        return '<Poem: %r %r >' % (self.title, self.content, self.userId)

    def to_json(self):
        feedbacks = [feedback.to_json_short() for feedback in self.feedbacks]
        poem_string = {
            'id': self.id, 
            'title': str(self.title), 
            'content': str(self.content),
            #Metodo para establecer la fecha y hora actual
            #Fecha enviada en un formato capaz de ser leido por el frontend
            'datePoem' : self.datePoem.strftime("%Y-%m-%d/%H:%M:%S"),
            #Elimino que retorne el userId, para que devuelva el usuario completo con todos los atributos
            'user': self.user.to_json_short(),
            'feedbacks' : feedbacks,
        }
        return (poem_string)
    def to_json_short(self):
        poem_json_short = {
            'id': self.id,
            'title': str(self.title),
            'content': str(self.content),
            'date' : self.date.strftime("%Y-%m-%d/%H:%M:%S"),
            #'userId' : self.user_id
        }
        return(poem_json_short)

    @staticmethod
    def from_json(json_string):
        id = json_string.get('id')
        title = json_string.get('title')
        content = json_string.get('content')
        userId = json_string.get('userId')
        
        return (Poem(id = id, title = title, content = content, userId = userId))
        