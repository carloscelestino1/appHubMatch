from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen


class MyScreen(Screen):
    def init(self, kwargs):
        super().init(kwargs)

        label = MDLabel(text="[ref=https://kivy.org]Visite o site do Kivy[/ref]", markup=True)
        self.add_widget(label)


class MyApp(MDApp):
    def build(self):
        return MyScreen()


MyApp().run()