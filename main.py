from flask import Flask, render_template, request, redirect
import webbrowser
import threading
from tratamentoDeErro import *
from bancoDeDados import *
from usuario import *

app = Flask(__name__,static_folder='static') # Instancia o Flask
bd = BancoDeDados() # Instancia o banco de dados

# Rota Inicial
@app.route("/", methods=["POST", "GET"])
def index():
    return redirect('/Login') # Redireciona para a tela de login
    

# Rota de Login
@app.route("/Login", methods=["POST", "GET"])
def tela_de_login():
    global usuario_logado
    # No if abaixo devemos inserir a comparação com o banco de dados, levando usuario e senha em consideração
    if request.method == 'POST':
        listaDeUsuarios = bd.ler_dados()
        email = request.form.get("email") # Obtém o email do campo de texto da tela de login
        senha = request.form.get("senha") # Obtém a senha do campo de texto da tela de login
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
        areas = request.form.getlist("areas") # Obtém as áreas do campo de texto da tela de cadastro
        projetos = request.form.getlist("projetos") # Obtém os projetos do campo de texto da tela de cadastro
        nome = request.form.get("nome") # Obtém o nome do campo de texto da tela de cadastro
        email = request.form.get("email") # Obtém o email do campo de texto da tela de cadastro
        senha = request.form.get("senha") # Obtém a senha do campo de texto da tela de cadastro
        confirmarSenha = request.form.get("confirmar_senha") # Obtém a confirmação de senha do campo de texto da tela de cadastro
        cargo = request.form.get("cargos") # Obtém o cargo do campo de texto da tela de cadastro

        try:
            verificar_senha(senha, confirmarSenha) 
        except VerificaErro as erroSenha: # Verifica todos os erros que podem englobar a senha
            return render_template('telaDeCadastro.html', erroSenha=erroSenha)
        
        try:
            verificar_cadastro_usuario(nome, email)
        except VerificaErro as erroEmail: # Verifica todos os erros que podem englobar o email
            return render_template('telaDeCadastro.html', erroEmail=erroEmail)
        
        try:
            verifica_preenchimento_dos_campos(areas, projetos)
        except VerificaErro as erroCampo: # Verifica todos os erros que podem englobar o preenchimento dos campos
            return render_template('telaDeCadastro.html', erroCampo=erroCampo)

        bd.inserir_usuario(nome, email, senha, cargo) # Insere o usuário no banco de dados caso não tenham havido erros

        for area in areas:
            bd.inserir_area(area, email) # Insere as áreas no banco de dados caso não tenham havido erros
        
        for projeto in projetos:
            bd.inserir_projeto(projeto, email) # Insere os projetos no banco de dados caso não tenham havido erros
        
        return redirect('/Login') # Redireciona para a tela de login após o cadastro bem-sucedido
    
    # Lógica da tela de cadastro
    return render_template('telaDeCadastro.html') # Renderiza a tela de cadastro por padrão


# Rota de Opções
@app.route('/Opcoes', methods=["POST", "GET"])
def telaDeOpcoes():
    return render_template('telaDoMenuDeOpcoes.html')  # Renderiza a tela de opções

estado = "Online" # Estado inicial do inserir horários
# Rota de inserir horários
@app.route('/editarHorarios', methods=['POST', 'GET'])
def editar_horarios():
    global estado

    if 'alterar_estado' in request.form: # Verifica se o botão de alterar estado foi pressionado
        if estado == "Online": # Altera o estado de acordo com o estado atual
            estado = "Presencial"
        else:# Altera o estado de acordo com o estado atual
            estado = "Online"

    if request.method == 'POST': # Verifica se o botão de salvar foi pressionado
        horarios_livre = request.form.getlist('horario')# Obtém os horários do campo de texto da tela de inserir horários
        if horarios_livre != []: # Verifica se o campo de texto não está vazio
            bd.inserir_horarios(usuario_logado.email, horarios_livre, estado)# Insere os horários no banco de dados

    return render_template('telaDeAdicaoDeHorarios.html', estado=estado) # Renderiza a tela de inserir horários

# Rota de criar reunião
@app.route('/criarReuniao', methods=['POST', 'GET'])
def criar_reuniao():
    #Página de criação de reunião
    return render_template('telaDeCriarReuniao.html')

# Rota Editar Tag
@app.route('/editarTAG', methods=['POST', 'GET'])
def editar_tag():
    areas = request.form.getlist("areas")# Obtém as áreas do campo de texto da tela de edição de tag
    projetos = request.form.getlist("projetos")# Obtém os projetos do campo de texto da tela de edição de tag
    if request.method == 'POST' and areas != []: # Verifica se o botão de salvar foi pressionado e se as áreas foram preenchidas
        bd.excluir_dado("area", "FK_area_usuario_email", usuario_logado.email) # Exclui as áreas do usuário para poder substituí-los
        for area in areas:
            bd.atualizar_area(area, usuario_logado.email) # Atualiza as áreas do usuário

    if request.method == 'POST' and projetos != []: #Repete a lógica de Areas
        bd.excluir_dado("projeto", "FK_projeto_usuario_email", usuario_logado.email)
        for projeto in projetos:
            bd.atualizar_projeto(projeto, usuario_logado.email)

    #Página de edição de tag
    return render_template('telaDeEditarTAG.html')

@app.route('/visualizar', methods=['POST', 'GET'])
def visualizar():
    global horarios_online
    global horarios_presenciais

    horarios_online = bd.ler_dados(tabela="horarios_online") # Obtém os horários online do banco de dados
    horarios_presenciais = bd.ler_dados(tabela="horarios_presencial") # Obtém os horários presenciais do banco de dados

    horarios_online_formatados = []  # Inicializa a lista de horários formatados para horários online
    horarios_presenciais_formatados = []  # Inicializa a lista de horários formatados para horários presenciais

    # Formate os horários de horários online
    for horario in horarios_online:
        horarios_divididos = [h.split('_') for h in horario[:6]] #Trata os horários para serem exibidos na tela
        email = horario[6] # Obtém o email do usuário
        horarios_online_formatados.append((horarios_divididos, email)) # Adiciona os horários formatados na lista de horários formatados

    # Formate os horários de horários presenciais, mesma lógica anterior
    for horario in horarios_presenciais:
        horarios_divididos = [h.split('_') for h in horario[:6]]
        email = horario[6]
        horarios_presenciais_formatados.append((horarios_divididos, email))

    # Renderiza a tela de visualização
    return render_template('telaDeVisualizacao.html', horarios_online=horarios_online_formatados, horarios_presenciais=horarios_presenciais_formatados)



# Função para iniciar o site
def inicia_site():
    app.run()

if __name__ == '__main__':
    # Inicia o site em uma thread separada, isso serve pra gnt iniciar o site direto, sem ter que ficar clicando em link
    threading.Thread(target=inicia_site).start()
    
    try:
        # Abre o navegador automaticamente na página local
        webbrowser.open("http://localhost:5000/")
        
    except Exception as erro: 
        print(str(erro))