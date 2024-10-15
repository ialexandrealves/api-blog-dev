# Criar estrutura inicial de tabelas autor e postagem C/ SQLAlchemy

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

#criar um API flask
app = Flask(__name__)
#Criar um instância de SQLAlchemy
app.config['SECRET_KEY']= 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
db:SQLAlchemy

#definir a estrutura da tabela Postagem
#id_postagem, titulo, autor
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer,db.ForeignKey('autor.id_autor'))
    #autor
# Definir a estrututa da tabela Autor
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.String)
    postagens = db.relationship('Postagem')
    
    
def inicializar_banco():
    #executar o comando para criar o banco de dados
    db.drop_all()
    db.create_all()
    #Criar usuários administradores
    autor = Autor(nome= 'lobi', email='lobi@gmail.com', senha='123456', admin=True)
    
    db.session.add(autor)
    db.session.commit()    

if __name__ == '__main__':
    inicializar_banco()     
