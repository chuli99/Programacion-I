from .. import db

class Poem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.String(500), nullable = False)
    userId = db.Column(db.Integer,db.ForeignKey('user.id'), nullable = False)

    def to_json(self):
        json_string = {
            'id': self.id, 
            'title': self.title, 
            'content': self.content,
            'userId': self.userId
        }
        return (json_string)
    
    
    @staticmethod
    def from_json(json_string):
        id = json_string.get('id')
        title = json_string.get('title')
        content = json_string.get('content')
        userId = json_string.get('UserId')
        return (Poem(id = id, title = title, content = content, userId = userId))
        