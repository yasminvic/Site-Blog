class User:
    def __init__(self, id, name, email, login, password):
        self.id = id,
        self.name = name,
        self.email = email,
        self.login = login,
        self.password = password

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'login': self.login,
            'password': self.password
        }
    
u1 = User(1, 'João de Souza', 'joao@gmail.com', 'jao', '123')
u2 = User(2, 'Maria de Souza', 'maria@gmail.com', 'maria', '123')
