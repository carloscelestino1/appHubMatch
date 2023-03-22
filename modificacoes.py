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
            MDIconButton:
                icon: "chevron-right"
                user_font_size: "35sp"
                pos_hint: {"center_x": .90, 'center_y': .9}
                on_release: app.root.current = 'welcomeScreen'
               
            Image:  
                source: 'LogoPrincipal.png'
                pos_hint: {'center_x': .5, 'center_y': .5}
                size_hint_max: 325, 325


            


<WelcomeScreen>:
    name: 'welcomeScreen'
    MDFloatLayout:
        md_bg_color : 1, 1, 1, 1
    Carousel:
        id: caraousel
        on_current_slide: app.current_slide(self.index)
        MDFloatLayout:
            MDIconButton:
                icon: "chevron-left"
                user_font_size: "35sp"
                pos_hint: {"center_y": .95}
                on_release: app.root.current = 'load'
            Image:
                source: "Hub1.jpg"
                pos_hint: {"center_x": .5, "center_y": .7}  
                size_hint_max: 330, 330
            MDLabel:
                pos_hint: {"center_y": .087}
                halign: "center"
                font_name: "Poppins-Light"
                font_size: "150sp"
                color: rgba(135, 143, 158, 200)    
        MDFloatLayout:
            Image:
                source: "Hub2.jpg"
                pos_hint: {"center_x": .5, "center_y": .7}  
                size_hint_max: 330, 330
            MDLabel:
                pos_hint: {"center_y": .087}
                halign: "center"
                font_name: "Poppins-Light"
                font_size: "14sp"
                color: rgba(135, 143, 158, 200)    
        MDFloatLayout:
            Image:
                source: "Hub3.jpg"
                pos_hint: {"center_x": .5, "center_y": .7} 
                size_hint_max: 330, 330
            MDLabel:
                pos_hint: {"center_y": .087}
                halign: "center"
                font_name: "Poppins-Light"
                font_size: "14sp"
                color: rgba(135, 143, 158, 200)
        MDFloatLayout:
            Image:
                source: "Hub5.jpg"
                pos_hint: {"center_x": .5, "center_y": .7}  
                size_hint_max: 330, 330
            MDLabel:
                pos_hint: {"center_y": .47}
                halign: "center"
                font_name: "Poppins-Regular"
                font_size: "25px"
                color: rgba(1, 3, 23, 225)
    
    MDBoxLayout:  
        MDFloatLayout:
            Image:
                source: "Vector.jpg"
                pos_hint: {"center_x": .5, "center_y": .4}  
            MDFillRoundFlatButton:
                md_bg_color: "#49C388"
                text: "Login"
                font_size:18
                text_color:1,1,1,1
                pos_hint: {'center_x': .5, 'center_y': .3}
                size_hint_x: .7

                on_release: app.root.current = 'login'
            
            MDFillRoundFlatButton:
                md_bg_color: "#49C388"
                text: "Cadastra-se"
                font_size:18
                text_color:1,1,1,1
                pos_hint: {'center_x': .5, 'center_y': .2}
                size_hint_x: .7

                on_release: app.root.current = 'whoAreyou'

            Image:  
                source: 'logosemnome.png'
                pos_hint: {'center_x': .5, 'center_y': .1}
                size_hint: .2, .2          




<Login>:
    name: 'login'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color:  "#49C388"  
        MDFloatLayout:
            MDIconButton:
                icon: "chevron-left"
                user_font_size: "35sp"
                pos_hint: {"center_x": .1, 'center_y': .9}
                on_release: app.root.current = 'welcomeScreen'
            Image:  
                source: 'HubMat.png'
                pos_hint: {'center_x': .5, 'center_y': .7}
                size_hint_max: 250, 250
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                mode: "round"
                line_color_focus: "black"
                icon_right: 'email'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                size_hint_x: .8
                hint_text: 'Email'
                pos_hint: {'center_x': .5, 'center_y': .4}
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                mode: "round"
                line_color_focus: "black"
                icon_right_color_focus: "49C388"
                icon_right: 'lock'
                icon_right_color_normal: "black"
                password: True
                size_hint_x: .8
                hint_text: 'Senha'
                pos_hint: {'center_x': .5, 'center_y': .3}
            MDTextButton:
                pos_hint: {'center_x': .5, 'center_y': .25}
                text: 'Esqueceu sua senha?'  
                text_color: "white"
                theme_text_color: "Custom"
            MDFillRoundFlatButton:
                md_bg_color: "000000"
                opacity: 0.73
                text: "Entrar"
                text_color: "white"
                font_size:14
                pos_hint: {'center_x': .7, 'center_y': .19}
                size_hint_x: .1 

                on_release: app.root.current
                    

                


<WhoAreyouHome>:
    name: 'whoAreyou'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: "#49C388"     
        MDFloatLayout:
            MDIconButton:
                icon: "chevron-left"
                user_font_size: "35sp"
                pos_hint: {"center_y": .95}
                on_release: app.root.current = 'welcomeScreen'
            Image:  
                source: 'MatchMilhoes.png'
                pos_hint: {'center_x': .5, 'center_y': .7}
                size_hint_max: 250, 250
            MDBoxLayout:  
            
            MDLabel:
                text: "Quem é você?"
                halign:'center'
                pos_hint: {'center_x': .5, 'center_y': .5}
                theme_text_color: "Custom"
                text_color: "white"
            MDFillRoundFlatButton:
                md_bg_color: "000000"
                opacity: 0.73
                text: "Startup"
                font_size:18
                text_color:1,1,1,1
                pos_hint: {'center_x': .5, 'center_y': .4}
                size_hint_x: .7

                on_release: app.root.current = 'register'

            MDFillRoundFlatButton:
                md_bg_color: "000000"
                opacity: 0.73
                text: "Investidor"
                font_size:18
                text_color:1,1,1,1
                pos_hint: {'center_x': .5, 'center_y': .3}
                size_hint_x: .7    
            MDFillRoundFlatButton:
                md_bg_color: "000000"
                opacity: 0.73
                text: "Mentor"
                font_size:18
                text_color:1,1,1,1
                pos_hint: {'center_x': .5, 'center_y': .2}
                size_hint_x: .7 
            MDFillRoundFlatButton:
                md_bg_color: "000000"
                opacity: 0.73
                text: "Cientista"
                text_color: "black"
                font_size:18
                text_color:1,1,1,1
                pos_hint: {'center_x': .5, 'center_y': .1}
                size_hint_x: .7      
                
<Register>:
    name: 'register'
    MDBoxLayout:
        orientation: 'vertical'        
        MDFloatLayout:
            MDIconButton:
                icon: "chevron-left"
                user_font_size: "35sp"
                pos_hint: {"center_y": .95}
                on_release: app.root.current = 'whoAreyou'
            Image:  
                source: 'LogoPrincipal.png'
                pos_hint: {'center_x': .5, 'center_y': .9}
                size_hint: .4, .4
            MDLabel:
                text: "STARTUP"
                halign:'center'
                pos_hint: {'center_x': .5, 'center_y': .77}
                text_color: "white"
            MDTextField:
                mode: "fill"
                size_hint_x: .9
                hint_text: 'CNPJ'
                pos_hint: {'center_x': .5, 'center_y': .7}
            MDTextField:
                mode: "fill"
                size_hint_x: .9
                hint_text: 'Razão Social'
                pos_hint: {'center_x': .5, 'center_y': .6}
            MDTextField:
                mode: "fill"
                size_hint_x: .9
                hint_text: 'E-mail'
                pos_hint: {'center_x': .5, 'center_y': .5}    
            MDTextField:
                mode: "fill"
                size_hint_x: .9
                hint_text: 'Senha'
                pos_hint: {'center_x': .5, 'center_y': .4}
            MDTextField:
                mode: "fill"
                size_hint_x: .9
                hint_text: 'Telefone'
                pos_hint: {'center_x': .5, 'center_y': .3}
            MDCheckbox:
                size_hint: None, None
                size: "48dp", "48dp"
                pos_hint: {'center_x': .1, 'center_y': .2}
            MDLabel:
                font_style: "Caption"
                text: "Li e concordo com os termos"
                halign:'center'
                pos_hint: {'center_x': .4, 'center_y': .2}
                text_color: "white"
                user_font_size: "10sp"
            MDFillRoundFlatButton:
                md_bg_color: "1F4935"
                opacity: 1
                text: "Cadastrar"
                text_color: "black"
                font_size:14
                text_color:1,1,1,1
                pos_hint: {'center_x': .8, 'center_y': .1}
                
                on_release: app.root.current = 'editprofile'



<EditProfile>:
    name: 'editprofile'
    MDBoxLayout:
        orientation: 'vertical'            
        MDFloatLayout: 
            MDIconButton:
                icon: "chevron-left"
                user_font_size: "35sp"
                pos_hint: {"center_y": .95}
                on_release: app.root.current = 'register'
            Image:  
                source: 'LogoPrincipal.png'
                pos_hint: {'center_x': .5, 'center_y': .9}
                size_hint: .4, .4
            MDTextField:
                size_hint_x: .4
                hint_text: "Nome"
                fill_color: 0, 0, 0, .4
                multiline: True
                pos_hint: {"center_x": .7, "center_y": .75}
            Image:  
                source: 'Ellipse2.png'
                pos_hint: {'center_x': .2, 'center_y': .75} 
            MDIconButton:
                icon: "download"
                pos_hint: {'center_x': .2, 'center_y': .7} 
                user_font_size: "35sp"    
            MDTextField:
                size_hint_x: .8
                size_hint_y: .1
                hint_text: "Bio"
                mode: "fill"
                fill_color: 0, 0, 0, .4
                multiline: True
                pos_hint: {"center_x": .5, "center_y": .58}
            MDTextField:
                size_hint_x: .8
                hint_text: "Vídeo de apresentação"
                text:"URL"
                mode: "fill"
                fill_color: 0, 0, 0, .4
                multiline: True
                pos_hint: {"center_x": .5, "center_y": .48}
            MDTextField:
                size_hint_x: .8
                hint_text: "Tags"
                mode: "fill"
                fill_color: 0, 0, 0, .4
                multiline: True
                pos_hint: {"center_x": .5, "center_y": .38}
            MDLabel:
                text: "Dados Bancarios"
                halign:'center'
                pos_hint: {'center_x': .27, 'center_y': .30}
            MDTextField:
                size_hint_x: .4
                hint_text: "Agência"
                mode: "round"
                pos_hint: {"center_x": .3, "center_y": .25}
            MDTextField:
                size_hint_x: .4
                hint_text: "Conta"
                mode: "round"
                pos_hint: {"center_x": .3, "center_y": .18}
            MDTextField:
                size_hint_x: .4
                hint_text: "Banco"
                mode: "round"
                pos_hint: {"center_x": .3, "center_y": .11}        
            MDFillRoundFlatButton:
                md_bg_color: "1F4935"
                opacity: 1
                text: "Concluir"
                text_color: "black"
                font_size:14
                text_color:1,1,1,1
                pos_hint: {'center_x': .8, 'center_y': .1}




''')



class JanelaGerenciadora(ScreenManager):
    pass

class Load(Screen):
    pass

class Login(Screen):
    pass

class WhoAreyouHome(Screen):
    pass

class Register(Screen):
    pass

class EditProfile(Screen):
    pass


class WelcomeScreen(Screen):

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
        self.janela_gerenciadora.current = 'register'
    
    def welcome_screen(self):
        self.janela_gerenciadora.current = 'welcomeScreen'

    def editprofile(self):
        self.janela_gerenciadora.current = 'editprofile'

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.janela_gerenciadora = JanelaGerenciadora()
        self.load = Load()
        self.login = Login()
        self.whoAreyouHome = WhoAreyouHome()
        self.register = Register()
        self.editprofile= EditProfile()
        self.welcome_screenn = WelcomeScreen()
        self.janela_gerenciadora.add_widget(self.load)
        self.janela_gerenciadora.add_widget(self.login)
        self.janela_gerenciadora.add_widget(self.whoAreyouHome)
        self.janela_gerenciadora.add_widget(self.register)
        self.janela_gerenciadora.add_widget(self.welcome_screenn)
        self.janela_gerenciadora.add_widget(self.editprofile)

        return self.janela_gerenciadora
    
MyApp().run()
