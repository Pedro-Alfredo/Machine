import hashlib

class Seguranca:
    def __init__(self):
        self.hash_senha = hashlib.sha256("admin123".encode()).hexdigest()

    def autenticar(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest() == self.hash_senha
