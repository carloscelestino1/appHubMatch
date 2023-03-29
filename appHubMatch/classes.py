from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog

Window.size = (350, 580)
 

class JanelaGerenciadora(ScreenManager):
    pass

class Load(Screen):    
    pass

class Login(Screen):
    pass

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

