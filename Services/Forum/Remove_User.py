from Models import Usuario

def remove_user(id):
    busca = None
    Retorno={'status':'', 'msg':'', 'data':''}
    cont = 0
    for  index in Usuario.Data_Usuario:
        if index['id'] == id['id']:
            del Usuario.Data_Usuario[cont]
            Retorno['status'] = 'OK'
            Retorno['msg'] = 'Usuario removido com sucesso!'
            Retorno['data'] = Usuario.Data_Usuario
            return Retorno
        cont =+1

    Retorno['status'] = 'FAIL'
    Retorno['msg'] = 'Usuario não encontrado!'
    Retorno['data'] = None
    return Retorno