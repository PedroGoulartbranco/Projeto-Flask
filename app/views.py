from app import app
from flask import render_template

@app.route('/')
def pagina_inicial():
    nome = "Pedro"
    return render_template('index.html', nome=nome)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro/usuario')
def cadastro_usuario():
    return render_template('cadastro_pessoa.html')