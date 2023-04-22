from configs.config import *

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    user_id = db.Column(db.Text)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    date = db.Column(db.Text)

    def json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description,
            "date": self.date
        }

