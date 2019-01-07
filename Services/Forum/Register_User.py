from Models import Usuario
import uuid

def form_user(Dados):
    id = uuid.uuid4()
    id = str(id.time_low)
    nome=Dados["nome"]
    Retorno ={
        'id':id, 
        'nome':nome, 
        }
    Usuario.Data_Usuario.append(Retorno)
    return Retorno