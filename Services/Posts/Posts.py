from Models import Postagem, Usuario

def listar_posts(Dados):
    Retorno = Retorno={'status':'', 'msg':'', 'data':[]}
    for index in Usuario.Data_Usuario:
        if Dados['id_usuario'] == index['id']:
            Retorno['status'] = 'OK'
            Retorno['msg'] = 'Lista de Posts recebida!'
            Retorno['data'] = Postagem.Data_Postagem
            return Retorno

    Retorno['status'] = 'FAIL'
    Retorno['msg'] = 'Usuario não identificado!'
    Retorno['data'] = None
    return Retorno