class SenhaInvalidaErro(Exception):
    def __init__(self, mensagens):
        self.mensagens = mensagens

def verificar_senha(senha, confirmaSenha):
    mensagens = []
    if len(senha) < 8:
        mensagens.append("A senha deve conter pelo menos 8 caracteres.")
    if not any(c.isupper() for c in senha):
        mensagens.append("A senha deve conter pelo menos um caractere maiúsculo.")
    if not any(c.islower() for c in senha):
        mensagens.append("A senha deve conter pelo menos um caractere minúsculo.")
    if not any(c.isdigit() for c in senha):
        mensagens.append("A senha deve conter pelo menos um dígito.")
    if senha != confirmaSenha:
        mensagens.append("A senha e sua confirmação devem ser iguais.")

    if mensagens:
        raise SenhaInvalidaErro(mensagens)
