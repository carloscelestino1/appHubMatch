
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window


Window.size = (350, 580)


Builder.load_string('''

 

<JanelaPrincipal>:
    name: 'janelaprincipal'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            size_hint: 1, .1
            elevation: 0
            md_bg_color: "49C388"
        MDFloatLayout:
            Image:
                source: "img/image4.png"
                pos_hint: {'center_x': 0.5,'center_y': 0.80}
                size_hint: 0.65, 0.33  
            MDTextField:              
                hint_text: "Pesquisar"
                mode: "round"
                icon_left: "magnify"
                pos_hint: {'center_x': .5,'center_y': .58}
                size_hint: 0.70, 0.07

            MDCard:
                id: 'Azul'
                elevation: 0
                md_bg_color:  0,0,0,0
                spacing: 15
                padding: 17
                size_hint: 0.7, 0.25
                pos_hint: {'center_x': .5,'center_y': 0.44}
                
                MDCard:
                    id: ''
                    elevation: 0
                    md_bg_color: "49C388"
                    ripple_behavior: True
                    Image:
                        source: "img/book.png"
                        elevation: 0
                MDCard:
                    id: ''
                    elevation: 0
                    md_bg_color: "49C388"
                    ripple_behavior: True
                    Image:
                        source: "img/money.png"
                        elevation: 0
                    
            MDCard:
                elevation: 0
                md_bg_color:  0,0,0,0
                spacing: 15
                padding: 17
                size_hint: 0.7, 0.25
                pos_hint: {'center_x': .5,'center_y': 0.23}
                
                MDCard:
                    id: ''
                    elevation: 0
                    md_bg_color: "49C388"
                    ripple_behavior: True
                    Image:
                        source: "img/music.png"
                        elevation: 0
                MDCard:
                    id: ''
                    elevation: 0
                    md_bg_color: "49C388"
                    ripple_behavior: True
                    Image:
                        source:"img/gast.png"
                        elevation: 0
            MDBottomNavigation:
                panel_color: "49C388"
                size_hint: 1, .06
                elevation: 0
                MDBottomNavigationItem:
                    icon:"cog"
                MDBottomNavigationItem:
                    icon:"forum" 
                MDBottomNavigationItem:
                    icon:"home"
                MDBottomNavigationItem:
                    icon:"magnify"                    
                MDBottomNavigationItem:
                    icon:"account-outline"        

<Janela1>:
    name: 'janela1'
    MDBoxLayout:
        md_bg_color: 'blue'
        orientation:'vertical'
            
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y:.75
            cols:2
            padding:[dp(15),dp(15),dp(15),dp(35)]
            spacing:dp(15)
            MDCard:
                on_release: app.guia_postural_press()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'fotomenu.png'
                        pos_hint: {'center_x': .13, 'center_y': .4}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'GUIA POSTURAL'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}

                
                                    
                
            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'segundaFoto.png'
                        pos_hint: {'center_x': .13, 'center_y': .6}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'EXERCÍCIO LABORAL'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'terceiraFoto.png'
                        pos_hint: {'center_x': .13, 'center_y': .6}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'INSATISFAÇÕES'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'quartaFoto.png'
                        pos_hint: {'center_x': .13, 'center_y': .5}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'FALE CONOSCO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}

            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'quintaFoto.png'
                        pos_hint: {'center_x': .13, 'center_y': .5}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'ANÁLISE DE POSTURA'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'sextaFoto.png'
                        pos_hint: {'center_x': .13, 'center_y': .5}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'QUESTIONÁRIO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            
            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'sextaFoto.png'
                        pos_hint: {'center_x': .13, 'center_y': .5}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_height: True
                        mode: 'fill'
                        text: 'FERRAMENTAS DE ACESSIBILIDADE'
                        
                        pos_hint: {'center_x': .18, 'center_y': .6}
                    

<GuiaPostural>:
    name: 'guia_postural'
    MDBoxLayout:
        md_bg_color: 'blue'
        orientation: 'vertical'
            
        MDBoxLayout:
            
            size_hint_y:.4
            cols:2
            padding:[dp(15),dp(15),dp(15),dp(35)]
            spacing:dp(15)
            MDCard:
                    
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                
                Image:
                    source: 'guia_post1.png'
                    pos_hint: {'center_x': .13, 'center_y': .5}

        MDBoxLayout:
            
            size_hint_y:.4
            cols:2
            padding:[dp(15),dp(15),dp(15),dp(35)]
            spacing:dp(15)
            MDCard:
                    
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                
                Image:
                    source: 'guia_post2.jpg'
                    pos_hint: {'center_x': .13, 'center_y': .5}

        MDBoxLayout:
            
            size_hint_y:.4
            cols:2
            padding:[dp(15),dp(15),dp(15),dp(35)]
            spacing:dp(15)
            MDCard:
                    
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                
                Image:
                    source: 'guia_post3.jpg'
                    pos_hint: {'center_x': .13, 'center_y': .5}

        MDBoxLayout:
            
            size_hint_y:.4
            cols:2
            padding:[dp(15),dp(15),dp(15),dp(35)]
            spacing:dp(15)
            MDCard:
                    
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                
                Image:
                    source: 'guia_post4.jpg'
                    pos_hint: {'center_x': .13, 'center_y': .5}    

''')

class JanelaGerenciadora(ScreenManager):
    pass

class JanelaPrincipal(Screen):
    pass

class Janela1(Screen):
    pass

class GuiaPostural(Screen):
    pass

class ExerLab(Screen):
    pass

class MyApp(MDApp):

    
    def change_color(self):
        theme = self.theme_cls.theme_style
        if theme == 'Dark':
            self.theme_cls.theme_style = 'Light'
        else:
            self.theme_cls.theme_style = 'Dark'

    def guia_postural_press(self):
        self.janela_gerenciadora.current = 'guia_postural'

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.janela_gerenciadora = JanelaGerenciadora()
        self.janela_principal = JanelaPrincipal()
        self.janela1 = Janela1()
        self.guia_postural = GuiaPostural()
        self.laboral_postural = ExerLab()
        self.janela_gerenciadora.add_widget(self.janela_principal)
        self.janela_gerenciadora.add_widget(self.janela1)
        self.janela_gerenciadora.add_widget(self.guia_postural)
        self.janela_gerenciadora.add_widget(self.laboral_postural)
        
        return self.janela_gerenciadora
    
MyApp().run()