from Models import Postagem, Forum, Usuario, Messages
from Services import Message
import datetime
import uuid
def form_post(Dados):
    Retorno={'status':'', 'msg':'', 'data':''}
    cont = 0
    id = uuid.uuid4()
    id = str((id.time_low))
    id_forum=Dados["id_forum"]
    id_criador = Dados["id_criador"]
    hora_envio = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    mensagem = Dados["mensagem"]
    visivel = Dados["visivel"]

    Data ={
        'id':id, 
        'id_forum':id_forum, 
        'id_criador':id_criador, 
        'hora_envio':hora_envio, 
        'mensagem':mensagem, 
        'visivel':visivel,
        }

    for index in Usuario.Data_Usuario:
        if Dados['id_criador'] == index['id']:
            for index in Forum.Data_Forum:
                if index['id'] == id_forum:
                    Forum.Data_Forum[cont]['hora_ultimo'] = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
                    Retorno['status'] = 'OK'
                    Retorno['msg'] = 'Post criado com sucesso'
                    Retorno['data'] = Data
                    Postagem.Data_Postagem.append(Data)
                    Message.Create_Messages(Data)
                    return Retorno
                cont = cont + 1
        
            Retorno['status'] = 'FAIL'
            Retorno['msg'] = 'Forum não encontrado'
            Retorno['data'] = None
            return Retorno

    Retorno['status'] = 'FAIL'
    Retorno['msg'] = 'Usuario não identificado!'
    Retorno['data'] = None
    return Retorno
            


