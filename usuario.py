
class Usuario:
    def __initi__(self, nome, email, senha, cargo, projeto, area, horarios_online=[], horarios_presencial=[]):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.projeto = projeto
        self.area = area
        self.horarios_online = horarios_online
        self.horarios_presencial = horarios_presencial

    def cadastrarNoSistema():
        pass

    def getTagDeFiltro(self):
        return [self.cargo, self.projeto, self.area]