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
from kivy.uix.button import Button



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

# verificação de email
def verificar_email(email):
    ref = db.reference('usuarios')
    usuarios = ref.get()
    
    for usuario_id in usuarios:
        usuario = usuarios[usuario_id]
        if usuario['email'] == email:
            return False
    return True

# registra informações no banco
def register(email,senha,telefone,tipoperfil):
        
        if verificar_email(email):
            if email =='' or senha =='' or telefone =='':
                dialog = MDDialog(
                    title="Atenção",
                    text="preencha todos os campos",
                    size_hint=(0.8, 0.4)
                    )
                dialog.open()
            else:
                
                dados = {

                    'email':email,
                    'senha':senha,
                    'telefone':telefone,
                    'nome':'',
                    'proposito':'',
                    'pdf':'',
                    'tags':tipoperfil,
                    'perfil': tipoperfil
                }

                ref = db.reference('/usuarios/')

                ref.push(dados)
                return True
        else:
            dialog = MDDialog(
                title="Atenção",
                text="email ja cadastrado",
                size_hint=(0.8, 0.4)
                )
            dialog.open()

 

# autenticação do google
class GoogleAuthManager:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.credentials = None
    
    def authenticate(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            'arquivos/client_secret.json',
            scopes=['https://www.googleapis.com/auth/userinfo.profile', 'openid', 'https://www.googleapis.com/auth/userinfo.email'])
        self.credentials = flow.run_local_server(port=0)
    
    def get_user_profile(self):
        if not self.credentials:
            return None
        
        service = build('oauth2', 'v2', credentials=self.credentials)
        profile = service.userinfo().get().execute()
        return profile


# abertura padrão da janela
Window.size = (350, 580)

class JanelaGerenciadora(ScreenManager):
    pass

class Load(Screen):    
    pass

class Login(Screen):

    def login_google(self):
        google_auth = GoogleAuthManager("67712586747-sej00u1bi25o394j29do33u1kg5ero3n.apps.googleusercontent.com", "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")
        google_auth.authenticate()
        profile = google_auth.get_user_profile()
        
        # Check if profile data was successfully retrieved
        if profile:
            # Print name and email
            print(f"Name: {profile['name']}")
            print(f"Email: {profile['email']}")
            self.manager.current = "filter"
        else:
            print("Failed to retrieve user profile.")

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
    def register_startup(self):
        email = self.ids.emails.text
        senha = self.ids.senhas.text
        telefone = self.ids.phones.text
        tipoperfil = 'Startup'
        if register(email,senha,telefone,tipoperfil):
            self.manager.current = "editprofile"
        
            
class Register_Investidor(Screen):
    def register_investidor(self):
        email = self.ids.emaili.text
        senha = self.ids.senhai.text
        telefone = self.ids.phonei.text
        tipoperfil = 'investidor'
        if register(email,senha,telefone,tipoperfil):
            self.manager.current = "editprofile"

class Register_Mentor(Screen):
    def register_mentor(self):
        email = self.ids.emailm.text
        senha = self.ids.senham.text
        telefone = self.ids.phonem.text
        tipoperfil = 'mentor'
        if register(email,senha,telefone,tipoperfil):
            self.manager.current = "editprofile"

class Register_Cientista(Screen):
    def register_cientista(self):
        email = self.ids.emailc.text
        senha = self.ids.senhac.text
        telefone = self.ids.phonec.text
        tipoperfil = 'cientista'
        if register(email,senha,telefone,tipoperfil):
            self.manager.current = "editprofile"

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

