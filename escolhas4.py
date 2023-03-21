from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

KV = '''
JanelaGerenciadora:

    JanelaPrincipal:

    Janela1:

    GuiaPostural:

<JanelaPrincipal>:
    name: 'janelaprincipal'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: "#49C388"     
        MDFloatLayout:
            MDIconButton:
                icon: "chevron-left"
                user_font_size: "35sp"
                pos_hint: {"center_y": .95}
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
    MDRaisedButton: 
        text: 'olá'

'''

class JanelaGerenciadora(ScreenManager):
    pass

class JanelaPrincipal(Screen):
    pass

class Janela1(Screen):
    pass

class GuiaPostural(Screen):
    pass

class MyApp(MDApp):
    
    def change_color(self):
        theme = self.theme_cls.theme_style
        if theme == 'Dark':
            self.theme_cls.theme_style = 'Light'
        else:
            self.theme_cls.theme_style = 'Dark'

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        return Builder.load_string(KV)
    
MyApp().run()