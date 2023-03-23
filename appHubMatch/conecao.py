import requests
import json


link = 'https://hubmatch-a524d-default-rtdb.firebaseio.com/'

dados = {
    'email':'teste3@hotmail.com',
    'senha':'teste3'
}

requisicao = requests.post(f'{link}/Registro/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

