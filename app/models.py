from app import db

class contato(db.Model):
    id = db.Colunm()
    nome = db.Colunm()
    email = db.Colunm()
    senha = db.Colunm()