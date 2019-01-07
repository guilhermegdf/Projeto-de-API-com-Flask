from Models import Forum, Usuario
from flask import jsonify
import datetime
import uuid

def form_forum(Dados):
    Retorno={'status':'', 'msg':'', 'data':''}
    id = uuid.uuid4()
    id = str((id.time_low))
    id_criador=Dados["id_criador"]
    titulo = Dados["titulo"]
    descricao = Dados["descricao"]
    hora_criacao = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    hora_ultimo = ''
    ativo = Dados["ativo"]
    Data ={
        'id':id, 
        'id_criador':id_criador, 
        'titulo':titulo, 
        'descricao':descricao, 
        'hora_criacao':hora_criacao, 
        'hora_ultimo':hora_ultimo,
        'ativo':ativo
        }
    for index in Usuario.Data_Usuario:
        if Data['id_criador'] == index['id']:
            Retorno['status'] = 'OK'
            Retorno['msg'] = 'Forum criado com sucesso'
            Retorno['data'] = Data
            Forum.Data_Forum.append(Data)
            return Retorno

    Retorno['status'] = 'FAIL'
    Retorno['msg'] = 'Usuario não identificado!'
    Retorno['data'] = None
    return Retorno