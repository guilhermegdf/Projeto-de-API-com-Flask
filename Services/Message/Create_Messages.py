from Models import Messages
from Services.Notification import NewNotification
def New_Message(Data):
    
    criar_msg={}
    criar_msg['id'] = Data['id']
    criar_msg['user_send'] = Data['id_criador']
    criar_msg['titulo'] = "Nova postagem no forum"+Data['id_forum']
    criar_msg['texto'] = Data['mensagem']
    criar_msg['hora_envio'] = Data['hora_envio']
    Messages.Data_Messages.append(criar_msg)
    New_Notification.nova_notificacao(Data, criar_msg['titulo'])
    return True