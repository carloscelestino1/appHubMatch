from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.core.window import Window

Window.size = (350, 580)
 
Builder.load_string('''

<Load>:
    name: 'load'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: "white" 
        MDFloatLayout:

                          
            MDCard:
                id: 'Azul'
                elevation: 0
                md_bg_color:  0,0,0,0
                spacing: 5
                padding: 5
                size_hint: 1, 0.30
                ripple_behavior: True
                pos_hint: {'center_x': .5,'center_y': .8}
                MDCard:
                    id: ''
                    elevation: 0
                    md_bg_color: 
                    padding: 10
                    size_hint: 1, 1
                    pos_hint: {'center_x': .5,'center_y': .5}
                    Image:
                        source: "img/FyTecLogo.png"
                        elevation: 0
                MDLabel:
                    ripple_behavior: True
                    pos_hint: {'center_x': 0.60,'center_y': 0.50}
                    text: "Fy.Tec"
                    
                    

                
                MDCard:
                    id: ''
                    elevation: 0
                    md_bg_color: 
                    ripple_behavior: True
                    pos_hint: {'center_x': .6,'center_y': 0.50}
                    Image:
                        source: "img/VectorHeart.png"
                        elevation: 0
            
            MDCard:
                id: 'Azul'
                elevation: 0
                md_bg_color:  0,0,0,0
                spacing: 5
                padding: 5
                size_hint: 1, 0.30
                ripple_behavior: True
                pos_hint: {'center_x': .5,'center_y': .58}
                MDCard:
                    id: ''
                    elevation: 0
                    md_bg_color: 
                    padding: 10
                    size_hint: 1, 1
                    pos_hint: {'center_x': .5,'center_y': .5}
                    Image:
                        source: "img/ILoveNetWork.png"
                        elevation: 0
                MDLabel:
                    ripple_behavior: True
                    pos_hint: {'center_x': 0.60,'center_y': 0.50}
                    text: "I Love Network"
                    
                    

                
                MDCard:
                    id: ''
                    elevation: 0
                    md_bg_color: 
                    ripple_behavior: True
                    pos_hint: {'center_x': .6,'center_y': 0.50}
                    Image:
                        source: "img/VectorHeart.png"
                        elevation: 0            
            


            
            
            
            
            
            
            
            MDBottomNavigation:
                panel_color: "49C388"
                size_hint: 1, .06
                elevation: 0                   
                MDBottomNavigationItem:
                    icon:"home"
                    on_tab_press: app.root.current = 'filter'
                MDBottomNavigationItem:
                    icon:"magnify"
                    on_tab_press: app.root.current = 'explorer'
                MDBottomNavigationItem:
                    icon:"heart-outline"
                    on_tab_press: app.root.current
                MDBottomNavigationItem:
                    icon:"forum"
                    on_tab_press: app.root.current = 'chat'       
                MDBottomNavigationItem:
                    icon:"account-outline"
                    on_tab_press: app.root.current = 'perfil'



''')


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


class Explorer(Screen):
    pass

class Chat(Screen):
    pass

class Filter(Screen):
    pass


class MyApp(MDApp):
    
        
    def current_slide(self, index):
        pass
    
    def change_color(self):
        theme = self.theme_cls.theme_style
        if theme == 'Dark':
            self.theme_cls.theme_style = 'Light'
        else:
            self.theme_cls.theme_style = 'Dark'

    def whoAreyouHome_press(self):
        self.janela_gerenciadora.current = 'whoAreyou'

    def register_press(self):
        self.janela_gerenciadora.current = 'register_startup'
    
    def register_press(self):
        self.janela_gerenciadora.current = 'register_investidor'
    
    def register_press(self):
        self.janela_gerenciadora.current = 'register_mentor'
    
    def register_press(self):
        self.janela_gerenciadora.current = 'register_cientista'
    
    def welcome_screen(self):
        self.janela_gerenciadora.current = 'welcomeScreen'
        
    def editprofile(self):
        self.janela_gerenciadora.current = 'editprofile'

    def perfil(self):
        self.janela_gerenciadora.current = 'perfil'
    

    def settingss_press(self):
        self.janela_gerenciadora.current = 'settings'

    
    def build(self):

        self.theme_cls.primary_palette = 'Blue'
        self.janela_gerenciadora = JanelaGerenciadora()
        self.load = Load()
        self.login = Login()
        self.whoAreyouHome = WhoAreyouHome()
        self.registers = Register_Startup()
        self.registeri = Register_Investidor()
        self.registerm = Register_Mentor()
        self.registerc = Register_Cientista()
        self.editprofilee= EditProfile()
        self.welcome_screenn = WelcomeScreen()
        self.explorer = Explorer()
        self.settingss = Settingss()
        self.chat = Chat()
        self.filter = Filter()
        self.perfill = Perfil()


        self.janela_gerenciadora.add_widget(self.load)
        self.janela_gerenciadora.add_widget(self.login)
        self.janela_gerenciadora.add_widget(self.whoAreyouHome)
        self.janela_gerenciadora.add_widget(self.registers)
        self.janela_gerenciadora.add_widget(self.registeri)
        self.janela_gerenciadora.add_widget(self.registerm)
        self.janela_gerenciadora.add_widget(self.registerc)
        self.janela_gerenciadora.add_widget(self.welcome_screenn)
        self.janela_gerenciadora.add_widget(self.editprofilee)
        self.janela_gerenciadora.add_widget(self.explorer)
        self.janela_gerenciadora.add_widget(self.settingss)
        self.janela_gerenciadora.add_widget(self.chat)
        self.janela_gerenciadora.add_widget(self.filter)
        self.janela_gerenciadora.add_widget(self.perfill)





        return self.janela_gerenciadora
    
MyApp().run()
