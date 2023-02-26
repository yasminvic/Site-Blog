from models.User import *
import datetime

class Post:
    def __init__(self, id, author, title, description, date):
        self.id = id
        self.author = author,
        self.title = title,
        self.description = description,
        self.date = date

    def json(self):
        return {
            'id': self.id,
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'date': self.date
        }

p1 = Post(1, u1.name, 'Top 10 melhores momentos', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', datetime.datetime.now())   
p2 = Post(2, u2.name, 'Top 10 piores momentos', 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', datetime.datetime.now())   



posts = []
posts.append(p1.json())
posts.append(p2.json())

