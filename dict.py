
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton

Builder.load_string('''
<HomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)
        MDCard:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(20)
            size_hint: None, None
            size: dp(300), dp(400)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDIconButton:
                icon: 'image.png'
                user_font_size: '64sp'
                on_release: app.goto_next_screen()
            MDLabel:
                text: 'Home Screen'
                font_style: 'H4'
                halign: 'center'
<NextScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)
        MDCard:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(20)
            size_hint: None, None
            size: dp(300), dp(400)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDIconButton:
                icon: 'image.png'
                user_font_size: '64sp'
                on_release: app.goto_home_screen()
            MDLabel:
                text: 'Next Screen'
                font_style: 'H4'
                halign: 'center'
''')

class HomeScreen(Screen):
    pass

class NextScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class MyApp(MDApp):
    def build(self):
        self.screen_manager = MyScreenManager()
        self.home_screen = HomeScreen(name='home')
        self.next_screen = NextScreen(name='next')
        self.screen_manager.add_widget(self.home_screen)
        self.screen_manager.add_widget(self.next_screen)
        return self.screen_manager

    def goto_next_screen(self):
        self.screen_manager.current = 'next'

    def goto_home_screen(self):
        self.screen_manager.current = 'home'

if __name__ == '__main__':
    MyApp().run()