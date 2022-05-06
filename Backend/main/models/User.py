from email.policy import default
from .. import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    role = db.Column(db.String(10),nullable = False, default=False)
    poems = db.relationship('Poem',back_populates = 'user', cascade = 'all, delete-orphan')
    feedbacks = db.relationship('Feedback',back_populates = 'user', cascade = 'all, delete-orphan')
    
    #Getter de password plana
    @property
    def plain_password(self):
        raise AttributeError('Password no permitida')
    
    #Setter de la password plana
    # calcula el hash y lo guarda en el atributo password
    @plain_password.setter
    def plain_password(self,password):
        self.password = generate_password_hash(password)
    
    #Validar password
    def validate_pass(self,password):
        return check_password_hash(self.password,password)


    def __repr__(self):
        return '<User: %r %r >' % (self.name, self.email, self.password)
    
    
    def to_json(self):
        #llamo al to_json_short, ya que se generaria un bucle infinito, porque poems muestra al usuario
        #y a su vez el usuario muestra al poem
        poems = [poem.to_json_short() for poem in self.poems]
        feedbacks = [feedback.to_json_short() for feedback in self.feedbacks]
        user_json = {
            'id': self.id, 
            'name': str(self.name), 
            'email': str(self.email),
            'password': str(self.password),
            #Se deben recorrer los poemas, ya que en la mayoria de los casos se van a tener varios poemas
            'poems' : poems,
            'poems_count' : len(poems),
            'feedbacks' : feedbacks,
            'feedbacks_count' : len(feedbacks),
        }
        return (user_json)
    
    def to_json_short(self):
        user_json_short = {
            'id': self.id,
            'name': str(self.name),
            'email': str(self.email),
            'poems_count' : len(self.poems),
            'feedbacks_count' : len(self.feedbacks),
        }
        return (user_json_short)

    @staticmethod
    def from_json(json_string):
        id = json_string.get('id')
        name = json_string.get('name')
        email = json_string.get('email')
        password = json_string.get('password')
        role = json_string.get('role')
        return (User(id = id, name = name, email = email, plain_password = password, role = role))