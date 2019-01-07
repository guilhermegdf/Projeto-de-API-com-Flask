from Models import Notifications, Postagem
import datetime

def nova_notificacao(Data, title):

    y={}

    forum_users=[]
    for x in Postagem.Data_Postagem:
        if x['id_forum'] == Data['id_forum']:
            forum_users.append(x['id_criador'])

    for i in x:
        y['user_send'] = i
        y['titulo'] = title
        y['hora_envio'] = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        y['status'] = 'enviado'
        Notifications.Data_Notification.append(y)
    return True