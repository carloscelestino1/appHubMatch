import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import requests

cred = credentials.Certificate('arquivos/hubmatch-a524d-firebase-adminsdk-e9h3j-1071a6fec4.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hubmatch-a524d-default-rtdb.firebaseio.com'
})

pesquisa = ''
ref = db.reference('usuarios')
usuarios = ref.get()
lista_usuarios = []
for usuario_id in usuarios:
    usuario = usuarios[usuario_id]['tags']
    usuariose = usuarios[usuario_id]['seguimento']
    if usuario == pesquisa or usuariose == pesquisa:
        lista_usuarios.append(usuario_id)  
print (lista_usuarios)
