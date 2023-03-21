from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


Builder.load_string('''


<JanelaPrincipal>:
    name: 'janelaprincipal'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color:  "#49C388"  
        MDFloatLayout:
            MDIconButton:
                icon: "chevron-left"
                user_font_size: "35sp"
                pos_hint: {"center_x": .1, 'center_y': .9}
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