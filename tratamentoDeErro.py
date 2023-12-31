from bancoDeDados import *

class VerificaErro(Exception):
    def __init__(self, mensagens=[]):
        self.mensagens = mensagens

def verificar_senha(senha, confirmaSenha):
    """Verifica se a senha atende a determinados critérios."""
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
        raise VerificaErro(mensagens)
    
def verificar_cadastro_usuario(nome, email):
    """Verifica se o nome de usuário e o email atendem a determinados critérios."""
    mensagens = []
    # Verifique se o nome de usuário não contém caracteres especiais
    if any(c.isdigit() for c in nome):
        mensagens.append("O nome de usuário deve conter apenas letras.")
    if not any(c.isupper() for c in nome):
        mensagens.append("O nome deve conter pelo menos um caractere maiúsculo.")
    # Verifique se o email contém ".com" e "@"
    if "@" not in email:
        mensagens.append("Email inválido")

    bancoDeDadosPraVerificarErro = BancoDeDados()
    emailsCadastrados = bancoDeDadosPraVerificarErro.ler_dados(colunas="email")
    nomesCadastrados = bancoDeDadosPraVerificarErro.ler_dados(colunas="nome")

    print(nomesCadastrados)

    for emails in emailsCadastrados:  
        if email in emails:
            mensagens.append("Email já cadastrado")

    for nomes in nomesCadastrados:  
        if nome.lower() in nomes[0].lower():
            mensagens.append("Nome já cadastrado, insira nome + apelido")

    bancoDeDadosPraVerificarErro.desconectar()

    if mensagens:
        raise VerificaErro(mensagens)
    
def verifica_preenchimento_dos_campos(area, projeto):
    """Verifica se as áreas e projetos foram selecionados."""
    mensagens = []
    if area == []:
        mensagens.append("Selecione pelo menos uma área.")
    if projeto == []:
        mensagens.append("Selecione pelo menos um projeto.")
    if mensagens:
        raise VerificaErro(mensagens)
