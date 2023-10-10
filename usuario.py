
class Usuario:
    def __initi__(self, nome, email, senha, cargo, projeto, area):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.projeto = projeto
        self.area = area

    def cadastrarNoSistema():
        pass

    def getTagDeFiltro(self):
        return [self.cargo, self.projeto, self.area]

    
