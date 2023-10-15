from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import webbrowser
import threading
from tratamentoDeErro import *
from bancoDeDados import *

app = Flask(__name__,static_folder='static')
bd = BancoDeDados()
# TO DO: REVISAR IMPLEMENTAÇÃO DA PAGINAÇÃO DIVIDIDA OU INSERIR TODAS EM UM LUGAR SÓ.

# Rota Inicial
@app.route("/", methods=["POST", "GET"])
def index():
    return redirect('/Login')
    

# Rota de Login
@app.route("/Login", methods=["POST", "GET"])
def tela_de_login():
    # No if abaixo devemos inserir a comparação com o banco de dados, levando usuario e senha em consideração
    if request.method == 'POST':
        listaDeUsuarios = bd.ler_dados()
        email = request.form.get("email")
        senha = request.form.get("senha")
        for usuario in listaDeUsuarios:
            if email ==  usuario[1] and senha == usuario[2]:
                # Redireciona para a tela de menu de opções se o login for bem-sucedido
                return redirect('/Opcoes')
    
    # Renderiza a tela de login por padrão ou em caso de falha no login
    return render_template("telaDeLogin.html", falha=True)

# Rota da tela de cadastro
@app.route('/Cadastro', methods=['POST', 'GET'])
def telaDeCadastro():
    
    # Obtém os dados dos campos de texto da tela de cadastro
    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")
    confirmarSenha = request.form.get("confirmar_senha")
    cargo = request.form.get("cargos")
    projeto = request.form.get("projetos")
    area = request.form.get("areas")

    if request.method == 'POST':
        try:
            verificar_senha(senha, confirmarSenha)
        except VerificaErro as erroSenha:
            return render_template('telaDeCadastro.html', erroSenha=erroSenha)
        
        try:
            verificar_cadastro_usuario(nome, email)
        except VerificaErro as erroEmail:
            return render_template('telaDeCadastro.html', erroEmail=erroEmail)

        bd.inserir_usuario("usuarios", str(nome), str(email), str(senha), str(cargo), str(projeto), str(area))
        return redirect('/Opcoes')
    # Lógica da tela de cadastro
    return render_template('telaDeCadastro.html')

# Rota de Opções
@app.route('/Opcoes', methods=["POST", "GET"])
def telaDeOpcoes():
    return render_template('telaDoMenuDeOpcoes.html')

# Rota de Editar horários online
@app.route('/editarHorariosOnline', methods=['POST', 'GET'])
def editar_horarios():
    print(request.form.getlist('horario')) #para pegar todos os checkboxes
    if request.method == 'POST':
        print(request.form.getlist('horario')) # pegar somente os checkboxes mmarcados

        return redirect('/editarHorariosPresencial')
    # Lógica para a página de edição de horários
    return render_template('telaDeAdicaoDeHorariosOnline.html')

# Rota de Editar horários presencial
@app.route('/editarHorariosPresencial', methods=["POST", "GET"])
def editar_horario_Presencial():
    if request.method == 'POST':
        return redirect('/Opcoes')
    # Lógica para a página de criação de reunião
    return render_template('telaDeAdicaoDeHorariosPresencial.html')

# Rota de criar reunião
@app.route('/criarReuniao')
def criar_reuniao():
    # Lógica para a página de criação de reunião
    return render_template('telaDeCriarReuniao.html')

# Rota Editar Tag
@app.route('/editarTAG')
def editar_tag():
    # Lógica para a página de edição de tag
    return render_template('telaDeEditarTAG.html')

# Rota de visualizar horários
@app.route('/visualizar')
def visualizar():
    # Lógica para a página de visualização
    return render_template('telaDeHorarios.html')

# Função para iniciar o site
def inicia_site():
    app.run()

if __name__ == '__main__':
    # Inicia o site em uma thread separada
    threading.Thread(target=inicia_site).start()
    
    try:
        # Abre o navegador automaticamente na página local
        webbrowser.open("http://localhost:5000/")
        
    except Exception as erro:
        print(str(erro))