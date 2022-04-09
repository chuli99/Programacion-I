from .. import db

class Poem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.String(500), nullable = False)
    userId = db.Column(db.Integer,db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return '<Poem: %r %r >' % (self.title, self.content, self.userId)

    def to_json(self):
        poem_string = {
            'id': self.id, 
            'title': str(self.title), 
            'content': str(self.content),
            'userId': self.userId,
        }
        return (poem_string)
    def to_json_short(self):
        poem_json = {
            'id': self.id,
            'title': str(self.title),
            'content': str(self.content),
            'userId': self.userId,

        }
        return(poem_json)

    @staticmethod
    def from_json(json_string):
        id = json_string.get('id')
        title = json_string.get('title')
        content = json_string.get('content')
        userId = json_string.get('userId')
        return (Poem(id = id, title = title, content = content, userId = userId))
        