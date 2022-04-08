
from .. import db

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_Id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable = False)
    poem_Id = db.Column(db.String(100), db.ForeignKey('poem.id'), nullable = False)
    qualifications = db.Column(db.String(100), nullable = False)
    comment = db.Column(db.String(100), nullable = False)



    def to_json(self):
        json_string = {
            'id': self.id, 
            'poem_Id': self.poem_Id, 
            'comment': self.commen
        } 
        return (json_string)

    
    @staticmethod
    def from_json(json_string):
        id = json_string.get('id')
        poem_Id = json_string.get('poem_Id')
        comment = json_string.get('comment')
        qualifications = json_string.get('qualifications')
        return (Feedback(id = id, poem_Id = poem_Id, comment = comment, qualifications = qualifications))