from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Banco PostgreSQL na Railway (seguro com variável de ambiente)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos
class Membro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    data_nascimento = db.Column(db.Date)

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    data = db.Column(db.Date)
    descricao = db.Column(db.Text)

@app.route('/')
def painel():
    membros = Membro.query.all()
    eventos = Evento.query.all()
    hoje = datetime.now().date()
    aniversariantes = [m for m in membros if m.data_nascimento and m.data_nascimento.month == hoje.month and m.data_nascimento.day == hoje.day]
    return render_template('painel.html', membros=membros, eventos=eventos, aniversariantes=aniversariantes)

if __name__ == '__main__':
    app.run(debug=True)
