import requests
import json


link = 'https://hubmatch-a524d-default-rtdb.firebaseio.com/'

dados = {
    'email':'teste4@hotmail.com',
    'senha':'teste4'
}

requisicao = requests.post(f'{link}/Registro/.json', data=json.dumps(dados))
print(requisicao)

