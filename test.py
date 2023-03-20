'''from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
'''
#KV = '''
'''<ScreenOne>:
    MDRaisedButton:
        text: 'next screen'

<ScreenTwo>:
    MDRaisedButton:
        text: 'Back'
'''
'''
class ScreenOne(MDScreenManager):
    pass

class ScreenTwo(MDScreenManager):
    pass

class MainApp(MDApp):

    def build(self):
        Builder.load_string(KV)
        sm = MDScreenManager()
        sm.get_screen(ScreenOne())
        return sm
    
MainApp().run()'''
