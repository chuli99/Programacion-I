from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)

    def to_json(self):
        json_string = {
            'id': self.id, 
            'name': self.name, 
            'email': self.email
        }
        return (json_string)
    
    
    @staticmethod
    def from_json(json_string):
        id = json_string.get('id')
        name = json_string.get('name')
        email = json_string.get('email')
        password = json_string.get('password')
        return (User(id = id, name = name, email = email, password = password))