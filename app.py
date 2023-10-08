from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import webbrowser
import threading

app = Flask(__name__)

# Cria um novo cliente e o conecta ao servidor
client = MongoClient('localhost', 27017, username="eduguiima", password='JkpNudzHYW1ddxGh')

db = client.flask_db
todos = db.todos

# TO DO: REVISAR IMPLEMENTAÇÃO DA PAGINAÇÃO DIVIDIDA OU INSERIR TODAS EM UM LUGAR SÓ.

# Rota Inicial
@app.route("/", methods=["POST", "GET"])
def index():
    return redirect('/Login')
    

# Rota de Login
@app.route("/Login", methods=["POST", "GET"])
def tela_de_login():
    if request.method == 'POST':
        # Redireciona para a tela de menu de opções se o login for bem-sucedido
        return redirect('/Opcoes')
    
    # Renderiza a tela de login por padrão ou em caso de falha no login
    return render_template("telaDeLogin.html")

# Rota da tela de cadastro
@app.route('/Cadastro', methods=['POST', 'GET'])
def telaDeCadastro():
    if request.method == 'POST':
        return redirect('/editarHorariosOnline')
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
        # client.admin.command('ping')
        
        # # Envia um ping para confirmar que a conexão foi bem sucedida
        # print("Pinged your deployment. You successfully connected to MongoDB!")
        # Abre o navegador automaticamente na página local
        webbrowser.open("http://localhost:5000/")
        
    except Exception as erro:
        print(str(erro))