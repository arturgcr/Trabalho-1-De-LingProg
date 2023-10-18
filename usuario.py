class Usuario:
    def __init__(self, nome, email, senha, cargo):
        """Classe usuario, reponsavel por facilitar as manipulações do usuario logado"""
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo