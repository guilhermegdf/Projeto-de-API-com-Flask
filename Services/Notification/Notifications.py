from Models import Notifications

def listar_notifications():
    notification_response=[{}]
    y={}
    for x in Notifications.Data_Notification:
        y['id'] = x['id']
        y['user_send'] = x['user_send']
        y['titulo'] = x['titulo']
        y['hora_envio'] = x['hora_envio']
        y['status'] = 'recebida'
        notification_response.append(y)
    
    return notification_response