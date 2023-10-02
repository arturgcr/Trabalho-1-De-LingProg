from flask import Flask, render_template, request

# Inicializa o Flask
app = Flask(__name__)

# Rota do login
@app.route("/login", methods=["POST"])
def telaDeLogin():
    return render_template("telaDeLogin.html")
