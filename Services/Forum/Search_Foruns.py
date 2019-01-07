from Models import Forum

def Search(id):
    busca = None
    Retorno={'status':'', 'msg':'', 'data':''}
    for busca in Forum.Data_Forum:
        if busca['id'] == id:
            Retorno['status'] = 'OK'
            Retorno['msg'] = 'Forum encontrado com sucesso'
            Retorno['data'] = busca
            return Retorno
    if busca['id'] != id:
        Retorno['status'] = 'FAIL'
        Retorno['msg'] = 'Forum não encontrado'
        Retorno['data'] = None
        return Retorno