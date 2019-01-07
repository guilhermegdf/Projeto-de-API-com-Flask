from Models import Postagem, Usuario

def buscar_post(id, Dados):
    Retorno={'status':'', 'msg':'', 'data':''}
    cont = 0
    for index in Usuario.Data_Usuario:
        if index['id'] == Dados['id_criador']:
            for index in Postagem.Data_Postagem:
                if index['id'] == id:
                    Retorno['status'] = 'OK'
                    Retorno['msg'] = 'Post encontrado com sucesso'
                    Retorno['data'] = index
                    return Retorno

            Retorno['status'] = 'FAIL'
            Retorno['msg'] = 'Post não encontrado'
            Retorno['data'] = None
            return Retorno

    Retorno['status'] = 'FAIL'
    Retorno['msg'] = 'Usuario não identificado'
    Retorno['data'] = None
    return Retorno