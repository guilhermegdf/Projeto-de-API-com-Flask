from Models import Notifications, Messages

def ler_notificacao(id):
    index = 0
    for x in Messages.Data_Messages:
        if x['id'] == id:
            Notifications.Data_Notification[index]['status'] = 'lida'
            return x
        index = index + 1