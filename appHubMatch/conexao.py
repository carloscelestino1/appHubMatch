from kivy.app import App
from kivy.uix.button import Button
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class GoogleAuthManager:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.credentials = None
    
    def authenticate(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json',
            scopes=['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email'])
        self.credentials = flow.run_local_server(port=0)
    
    def get_user_profile(self):
        if not self.credentials:
            return None
        
        service = build('oauth2', 'v2', credentials=self.credentials)
        profile = service.userinfo().get().execute()
        return profile

class MyGoogleApp(App):
    def build(self):

        google_auth = GoogleAuthManager("67712586747-sej00u1bi25o394j29do33u1kg5ero3n.apps.googleusercontent.com", "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")
        btn_login = Button(text='Login with Google')
        btn_login.bind(on_press=lambda _: self.handle_login(google_auth))
        return btn_login
    
    def handle_login(self, google_auth):
        google_auth.authenticate()
        profile = google_auth.get_user_profile()
        # Use the user's profile data to customize the app UI or perform other actions.
        print(profile)

MyGoogleApp().run()
