from classes import *


class MyApp(MDApp):


    def on_start(self):
    
        Clock.schedule_once(self.change_screen, 6)

    def change_screen(self, dt):    
        self.janela_gerenciadora.current = "welcomeScreen"
        
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

    def match(self):
        self.janela_gerenciadora.current = 'match'

    
    def build(self):
        Builder.load_file('cod.kv')

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
        self.matchh = MatchScreem()


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
        self.janela_gerenciadora.add_widget(self.matchh)




        return self.janela_gerenciadora
    
MyApp().run()
