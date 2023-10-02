from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import webbrowser
import threading
from telaDeLogin import *

app = Flask(__name__)


# Cria um novo cliente e o conecta ao servidor
client = MongoClient('localhost', 27017, username="eduguiima", password='JkpNudzHYW1ddxGh')

db = client.flask_db
todos = db.todos

@app.route('/', methods=('GET', 'POST'))
def inicio():
    return render_template("telaDeLogin.html")

def Login():
    # Verifica se o botão de cadastro foi apertado
    pass
    

@app.route('/Cadastro')
def Cadastro():
    return render_template("telaDeCadastro.html")

# Função para iniciar o site
def inicia_site():
    app.run()

if __name__ == '__main__':
    # Inicia o site em uma thread separada
    threading.Thread(target=inicia_site).start()
    
    try:
        client.admin.command('ping')
        
        # Envia um ping para confirmar que a conexão foi bem sucedida
        print("Pinged your deployment. You successfully connected to MongoDB!")
        # Abre o navegador automaticamente na página local
        webbrowser.open("http://localhost:5000/")
        
    except Exception as erro:
        print(str(erro))