from flask import Flask, render_template, request, url_for, redirect, session, jsonify
import webbrowser
import threading
from tratamentoDeErro import *
from bancoDeDados import *
from usuario import *

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
    global usuario_logado
    # No if abaixo devemos inserir a comparação com o banco de dados, levando usuario e senha em consideração
    if request.method == 'POST':
        listaDeUsuarios = bd.ler_dados()
        email = request.form.get("email")
        senha = request.form.get("senha")
        for usuario in listaDeUsuarios:
            if email ==  usuario[1] and senha == usuario[2]:
                usuario_logado = Usuario(usuario[0], usuario[1], usuario[2], usuario[3]) #nome, email, senha, cargo
                # Redireciona para a tela de menu de opções se o login for bem-sucedido
                return redirect('/Opcoes')
    
    # Renderiza a tela de login por padrão ou em caso de falha no login
    return render_template("telaDeLogin.html", falha=True)



# Rota da tela de cadastro
@app.route('/Cadastro', methods=['POST', 'GET'])
def telaDeCadastro():
    if request.method == 'POST':
        # Obtém os dados dos campos de texto da tela de cadastro
        areas = request.form.getlist("areas")
        projetos = request.form.getlist("projetos")
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        confirmarSenha = request.form.get("confirmar_senha")
        cargo = request.form.get("cargos")

        try:
            verificar_senha(senha, confirmarSenha)
        except VerificaErro as erroSenha:
            return render_template('telaDeCadastro.html', erroSenha=erroSenha)
        
        try:
            verificar_cadastro_usuario(nome, email)
        except VerificaErro as erroEmail:
            return render_template('telaDeCadastro.html', erroEmail=erroEmail)
        
        try:
            verifica_preenchimento_dos_campos(areas, projetos)
        except VerificaErro as erroCampo:
            return render_template('telaDeCadastro.html', erroCampo=erroCampo)

        bd.inserir_usuario(nome, email, senha, cargo)

        for area in areas:
            bd.inserir_area(area, email)
        
        for projeto in projetos:
            bd.inserir_projeto(projeto, email)
        
        return redirect('/Login')
    
    # Lógica da tela de cadastro
    return render_template('telaDeCadastro.html')


# Rota de Opções
@app.route('/Opcoes', methods=["POST", "GET"])
def telaDeOpcoes():
    return render_template('telaDoMenuDeOpcoes.html')

estado = "Online"
@app.route('/editarHorarios', methods=['POST', 'GET'])
def editar_horarios():
    global estado

    if 'alterar_estado' in request.form:
        if estado == "Online":
            estado = "Presencial"
        else:
            estado = "Online"

    if request.method == 'POST':
        horarios_livre = request.form.getlist('horario')
        if horarios_livre != []: 
            bd.inserir_horarios(usuario_logado.email, horarios_livre, estado)

    return render_template('telaDeAdicaoDeHorarios.html', estado=estado)

# Rota de criar reunião
@app.route('/criarReuniao', methods=['POST', 'GET'])
def criar_reuniao():

    # Lógica para a página de criação de reunião
    return render_template('telaDeCriarReuniao.html')

# Rota Editar Tag
@app.route('/editarTAG', methods=['POST', 'GET'])
def editar_tag():
    areas = request.form.getlist("areas")
    projetos = request.form.getlist("projetos")
    if request.method == 'POST' and areas != []:
        bd.excluir_dado("area", "FK_area_usuario_email", usuario_logado.email)
        for area in areas:
            bd.atualizar_area(area, usuario_logado.email)

    if request.method == 'POST' and projetos != []:
        bd.excluir_dado("projeto", "FK_projeto_usuario_email", usuario_logado.email)
        for projeto in projetos:
            bd.atualizar_projeto(projeto, usuario_logado.email)

    # Lógica para a página de edição de tag
    return render_template('telaDeEditarTAG.html')

@app.route('/visualizar', methods=['POST', 'GET'])
def visualizar():
    global horarios
    horarios=[]
    horarios_formatados = []
    if not horarios:
        horarios = bd.ler_dados(tabela="horarios_online")

    horarios_formatados = []  # Inicializa a lista de horários formatados

    if request.method == 'POST':
        elemento_de_filtro = request.form.get('pesquisa')
        if elemento_de_filtro != '':
            # Filtra a lista de horários com base no termo de pesquisa
            horarios_filtrados = [horario for horario in horarios if elemento_de_filtro.lower() in horario[6].lower()]

            # Formate os horários filtrados
            for horario in horarios_filtrados:
                horarios_divididos = [h.split('_') for h in horario[:6]]
                email = horario[6]
                horarios_formatados.append((horarios_divididos, email))

    return render_template('telaDeVisualizacao.html', horarios=horarios_formatados)

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