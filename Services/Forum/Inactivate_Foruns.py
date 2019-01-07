from Models import Forum, Usuario

def Change(Dados):
    Retorno={'status':'', 'msg':'', 'data':''}
    cont = 0

    for index in Usuario.Data_Usuario:
        if index['id'] == Dados['id_criador']:

            for index in Forum.Data_Forum:
                if index['id'] == Dados['id']:
                    Forum.Data_Forum[cont]['ativo'] = False
                    Retorno['status'] = 'OK'
                    Retorno['msg'] = 'Forum ativado com sucesso'
                    Retorno['data'] = index
                    return Retorno
                cont = cont+1

            Retorno['status'] = 'FAIL'
            Retorno['msg'] = 'Forum não encontrado'
            Retorno['data'] = None
            return Retorno

    Retorno['status'] = 'FAIL'
    Retorno['msg'] = 'Somente o criador pode Desativar'
    Retorno['data'] = None
    return Retorno