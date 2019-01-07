from Server import app
from flask import jsonify
from flask import request
from Models import Resposta, Forum, Usuario, Postagem, Messages
from Services.Forum import Foruns, Create_Foruns, Search_Foruns, Activate_Foruns, Inactivate_Foruns, Register_User, Remove_User
from Services.Posts import Create_Post, Posts, Read_Post
from Services.Notification import Notifications,NewNotification, ReadNotification, DeleteNotification, ArchiveNotification
import jwt
import uuid
import datetime
import requests
from urllib.parse import urlparse

@app.route('/forum', methods=['GET'])
def foruns():
    Resposta.response['status'] = 'OK'
    Resposta.response['msg'] = 'Consulta realizada com sucesso!'
    Resposta.response['data'] = Foruns.listar_foruns()
    return jsonify(Resposta.response)

@app.route('/forum', methods=['POST'])
def create_foruns():
    Dados = request.get_json()
    Resultado = Create_Foruns.form_forum(Dados)
    Resposta.response['status'] = Resultado['status']
    Resposta.response['msg'] = Resultado['msg']
    Resposta.response['data'] = Resultado['data']
    return jsonify(Resposta.response)

@app.route('/forum/<id>', methods=['GET'])
def buscar_foruns(id):
    Resultado = Search_Foruns.Search(id)
    Resposta.response['status'] = Resultado['status']
    Resposta.response['msg'] = Resultado['msg']
    Resposta.response['data'] = Resultado['data']
    return jsonify(Resposta.response)

@app.route('/forum/inactivate', methods=['POST'])
def inactivate_foruns():
    Dados = request.get_json()
    Resultado = Inactivate_Foruns.Change(Dados)
    Resposta.response['status'] = Resultado['status']
    Resposta.response['msg'] = Resultado['msg']
    Resposta.response['data'] = Resultado['data']
    return jsonify(Resposta.response)

@app.route('/forum/activate', methods=['POST'])
def activate_foruns():
    Dados = request.get_json()
    Resultado = Activate_Foruns.Change(Dados)
    Resposta.response['status'] = Resultado['status']
    Resposta.response['msg'] = Resultado['msg']
    Resposta.response['data'] = Resultado['data']
    return jsonify(Resposta.response)

@app.route('/forum/register', methods=['POST'])
def create_user():
    Dados = request.get_json()
    Resposta.response['status'] = 'OK'
    Resposta.response['msg'] = 'Cadastro realizado com sucesso!'
    Resposta.response['data'] = Register_User.form_user(Dados)
    return jsonify(Resposta.response)

@app.route('/forum/unregister', methods=['POST'])
def delete_user():
    Dados = request.get_json()
    Resultado = Remove_User.remove_user(Dados)
    Resposta.response['status'] = Resultado['status']
    Resposta.response['msg'] = Resultado['msg']
    Resposta.response['data'] = Resultado['data']
    return jsonify(Resposta.response)

@app.route('/forum/post', methods=['GET'])
def posts():
    Dados = request.args
    Resultado = Posts.listar_posts(Dados)
    Resposta.response['status'] = Resultado['status']
    Resposta.response['msg'] = Resultado['msg']
    Resposta.response['data'] = Resultado['data']
    return jsonify(Resposta.response)

@app.route('/forum/post', methods=['POST'])
def create_post():
    Dados = request.get_json()
    Resultado = Create_Post.form_post(Dados)
    Resposta.response['status'] = Resultado['status']
    Resposta.response['msg'] = Resultado['msg']
    Resposta.response['data'] = Resultado['data']
    return jsonify(Resposta.response)

@app.route('/forum/post/<id>', methods=['GET'])
def read_post(id):
    Dados = request.args
    Resultado = Read_Post.buscar_post(id, Dados)
    Resposta.response['status'] = Resultado['status']
    Resposta.response['msg'] = Resultado['msg']
    Resposta.response['data'] = Resultado['data']
    return jsonify(Resposta.response)

@app.route('/auth', methods=['GET'])
def auth():
    if 'nome' in request.hearders and 'senha' in request.hearders:
        for i in Usuario.Data_Usuario:
            if i['nome'] == request.hearders['nome'] and i['senha'] == request.hearders['senha']:
                key = "ChaveSecreta"
                info = {"id":1010, "expiration":datetime.timedelta(minutes=10)}
                token = jwt.encode(info, key)
                return jsonify({"token": token.decode("UTF-8")})

@app.route('/messages', methods=['POST'])
def send_message():
    
    Data={
        'id':str((uuid.uuid4().time_low)),
        'user_send':Usuario.Data_Usuario[0]['nome'],
        'user_to':Usuario.Data_Usuario[1]['id'],
        'titulo':'Teste de notification',
        'texto':'Teste de notification msg',
        'hora_envio':datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"),
    }

    Messages.Data_Messages.append(Data)
    NewNotification.nova_notificacao(Data)
    Resposta.response['status'] = 'OK'
    Resposta.response['msg'] = 'Enviado com sucesso!'
    Resposta.response['data'] = Data
    return jsonify(Resposta.response)

@app.route('/notification', methods=['GET'])

def read_notification():
    if 'id' in request.hearders:
        Resposta.response['status'] = 'OK'
        Resposta.response['msg'] = 'Consulta realizada com sucesso!'
        Resposta.response['data'] = ReadNotification.ler_notificacao(id)
        return jsonify(Resposta.response)

def list_notifications():
    Resposta.response['status'] = 'OK'
    Resposta.response['msg'] = 'Consulta realizada com sucesso!'
    Resposta.response['data'] = Notifications.listar_notifications()
    return jsonify(Resposta.response)

@app.route('/notification/delete', methods=['DELETE'])
def delete_notification():
    if 'id' in request.hearders:
        Resposta.response['status'] = 'OK'
        Resposta.response['msg'] = 'Deletada com sucesso!'
        Resposta.response['data'] = DeleteNotification.deletar_notificacao(id)
        return jsonify(Resposta.response)

@app.route('/notification/archive', methods=['PUT'])
def archive_notification():
    if 'id' in request.hearders:
        Resposta.response['status'] = 'OK'
        Resposta.response['msg'] = 'Arquivada com sucesso!'
        Resposta.response['data'] = ArchiveNotification.arquivar_notificacao(id)
        return jsonify(Resposta.response)