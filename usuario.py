
class Usuario:
    def __init__(self, nome, email, senha, cargo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo

    def cadastrarNoSistema():
        pass

    def getTagDeFiltro(self):
        return [self.cargo, self.projeto, self.area]