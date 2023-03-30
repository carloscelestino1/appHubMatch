from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.core.window import Window
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import requests
from kivy.uix.popup import Popup
from kivymd.uix.dialog import MDDialog
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


from kivyauth.google_auth import initialize_google, login_google, logout_google

# credenciais de acesso ao banco
cred = credentials.Certificate('arquivos/hubmatch-a524d-firebase-adminsdk-e9h3j-1071a6fec4.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hubmatch-a524d-default-rtdb.firebaseio.com'
})

# função de verificação de dados no banco
def verificar_credenciais(email, senha):
    ref = db.reference('usuarios')
    usuarios = ref.get()

    for usuario_id in usuarios:
        usuario = usuarios[usuario_id]
        if usuario['email'] == email and usuario['senha'] == senha:
            return True

    return False


# abertura padrão da janela
Window.size = (350, 580)
 

class JanelaGerenciadora(ScreenManager):
    pass

class Load(Screen):    
    pass

class Login(Screen):

    def login(self):
        username = self.ids.email.text
        password = self.ids.senha.text
        if verificar_credenciais(username, password):
            self.manager.current = "filter"
        else:
            self.ids.email.text = ""
            self.ids.senha.text = ""
            dialog = MDDialog(
                title="Atenção",
                text="login ou senha incorretos",
                size_hint=(0.8, 0.4)
                )
            dialog.open()


class WhoAreyouHome(Screen):
    pass

class Register_Startup(Screen):
    pass

class Register_Investidor(Screen):
    pass

class Register_Mentor(Screen):
    pass

class Register_Cientista(Screen):
    pass

class EditProfile(Screen):
    pass


class Settingss(Screen):
    pass

class Perfil(Screen):
    pass


class Explorer(Screen):
    pass

class Chat(Screen):
    pass

class Filter(Screen):
    pass

class WelcomeScreen(Screen):

    def on_enter(self):
        Clock.schedule_interval(self.start_autorotation, 3)

    def start_autorotation(self, dt):
        carousel = self.ids.caraousel
        if carousel.index == len(carousel.slides) - 1:
            carousel.load_slide(carousel.slides[0])
        else:
            carousel.load_next()

    def stop_autorotation(self):
        Clock.unschedule(self.start_autorotation)

