from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    poems = db.relationship('Poem',back_populates = 'user', cascade = 'all, delete-orphan')

    def __repr__(self):
        return '<User: %r %r >' % (self.name, self.email, self.password)


    def to_json(self):
        #llamo al to_json_short, ya que se generaria un bucle infinito, porque poems muestra al usuario
        #y a su vez el usuario muestra al poem
        poems = [poem.to_json_short() for poem in self.poems]
        user_json = {
            'id': self.id, 
            'name': str(self.name), 
            'email': str(self.email),
            'password': str(self.password),
            #Se deben recorrer los poemas, ya que en la mayoria de los casos se van a tener varios poemas
            'poems' : poems
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