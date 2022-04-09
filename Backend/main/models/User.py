from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    
    def __repr__(self):
        return '<User: %r %r >' % (self.name, self.email, self.password)


    def to_json(self):
        user_json = {
            'id': self.id, 
            'name': str(self.name), 
            'email': str(self.email),
            'password': str(self.password),
        }
        return (user_json)
    
    def to_json_short(self):
        user_json = {
            'id': self.id,
            'name': str(self.name),
            'email': str(self.email),
        }
        return user_json

    @staticmethod
    def from_json(json_string):
        id = json_string.get('id')
        name = json_string.get('name')
        email = json_string.get('email')
        password = json_string.get('password')
        return (User(id = id, name = name, email = email, password = password))