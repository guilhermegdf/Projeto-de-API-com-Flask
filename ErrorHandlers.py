from Server import app
from Models import Resposta
from flask import jsonify


@app.errorhandler(500)
def TratarServerError(error):
    Resposta.response["status"] = "Erro"
    Resposta.response["msg"] = "Houve um erro interno no servidor, desculpe-nos pelo transtorno. Detalhe: {}".format(error)
    Resposta.response["data"] = ""
    return jsonify(Resposta.response)


@app.errorhandler(404)
def TratarNotFound(error):
    Resposta.response["status"] = "Erro"
    Resposta.response["msg"] = "Acao nao disponivel"
    Resposta.response["data"] = ""
    return jsonify(Resposta.response)