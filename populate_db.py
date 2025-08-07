from app import db, Membro, Evento
from datetime import datetime

m1 = Membro(nome="João Silva", email="joao@exemplo.com", data_nascimento=datetime(1985, 8, 5))
m2 = Membro(nome="Ana Costa", email="ana@exemplo.com", data_nascimento=datetime(1990, 3, 22))
e1 = Evento(nome="Encontro Nacional", data=datetime(2025, 9, 15), descricao="Grande evento anual dos motoclubes.")

db.session.add_all([m1, m2, e1])
db.session.commit()

print("Dados adicionados com sucesso!")
