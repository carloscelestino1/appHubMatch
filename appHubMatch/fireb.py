import requests
import json

# URL do Firebase onde você deseja enviar o POST
#url = 'https://hubmatch-a524d-default-rtdb.firebaseio.com/.json'
# Dados que você deseja enviar
#data = {'id': '1234', 'nome': 'João', 'sobrenome': 'Silva'}

#data = {
#    'id': '2222', 'nome': 'João', 'sobrenome': 'Silva'
#  }
 

# Convertendo o dicionário em um objeto JSON
#json_data = json.dumps(data)

# Fazendo a solicitação POST ao Firebase com o ID especificado
# response = requests.post(url=url, data=json_data)

# Verificando o status da solicitação
#if response.status_code == 200:
#    print('POST com sucesso!')
#else:
#    print('Falha ao enviar o POST')

#request = requests.get(url=url, data=json_data)
#dicts = json.loads(request.content)

#for d in dicts:
#    request = requests.get(url= f"https://hubmatch-a524d-default-rtdb.firebaseio.com/{d}.json", data=json_data)
#    dados = json.loads(request.content)   
#    if dados['id']=='2222':
#        print('liberado')


import firebase_admin
from firebase_admin import credentials, db

# Inicializar o SDK do Firebase
cred = credentials.Certificate('appHubMatch/hubmatch-a524d-firebase-adminsdk-e9h3j-1071a6fec4.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hubmatch-a524d-default-rtdb.firebaseio.com'
})


# Referência à coleção onde você deseja adicionar o objeto
ref = db.reference('/teste1/seila')
# Dados que você deseja adicionar ao objeto
data = {'nome': 'João', 'sobrenome': 'Silva'}

# Adicionando o objeto à coleção com uma chave exclusiva gerada automaticamente
new_obj_ref = ref.push(data)

# Imprimindo a chave gerada automaticamente para o novo objeto
#print(new_obj_ref.key)




