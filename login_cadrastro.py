from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager, NoTransition
from kivy.utils import rgba
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import Clock

Window.size = (310, 580)

class WelcomeScreen(Screen):
    pass

class AppApp(MDApp):
    def build(self):
        Builder.load_file('app.kv')
        return WelcomeScreen()

    def on_start(self):
        # Access the carousel.
        carousel = self.root.ids.caraousel
        # Set infinite looping (optional).
        carousel.loop = True
        # Schedule after every 3 seconds.
        Clock.schedule_interval(carousel.load_next, 3.0)


    def current_slide(self, index):
        pass

AppApp().run()