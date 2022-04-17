
from .. import db
from datetime import datetime

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,db.ForeignKey('user.id'), nullable = False)
    poemId = db.Column(db.String(100), db.ForeignKey('poem.id'), nullable = False)
    qualification = db.Column(db.Integer, nullable = False)
    comment = db.Column(db.String(100), nullable = False)
    user = db.relationship('User', back_populates = "feedbacks", uselist = False, single_parent = True)
    poem = db.relationship('Poem', back_populates = "feedbacks", uselist = False, single_parent = True)  
  
    def __repr__(self):
        return '<Feedback: %r %r >' % (self.userId, self.poemId, self.qualification,self.comment)

    def to_json(self):
        feedback_string = {
            'id': self.id, 
            'userId': self.userId,
            'poemId': self.poemId,
            'qualification': self.qualification, 
            'comment': str(self.comment),
            'user' : self.poem.to_json_short(),
            'poem' : self.poem.to_json_short(),
        } 
        return (feedback_string)

    def to_json_short(self):
        feedback_json = {
            'id': self.id, 
            #'userId': self.userId,
            #'poemId': self.poemId,
            'qualification': self.qualification, 
            'comment': str(self.comment),
        }
        return (feedback_json)

    @staticmethod
    def from_json(json_string):
        id = json_string.get('id')
        userId = json_string.get('userId')
        poemId = json_string.get('poemId')
        comment = json_string.get('comment')
        qualification = json_string.get('qualification')
        return (Feedback(id = id, userId = userId ,poemId = poemId, comment = comment, qualification = qualification))