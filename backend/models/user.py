from configs.config import *

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    login = db.Column(db.Text)
    password = db.Column(db.Text)

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "login": self.login,
            "password": self.password
        }
    
