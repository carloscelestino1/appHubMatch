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
                source: 'img/LogoPrincipal.png'
                pos_hint: {'center_x': .5, 'center_y': .5}
                size_hint_max: 325, 325

<WelcomeScreen>:
    name: 'welcomeScreen'
    MDFloatLayout:
        md_bg_color: 1,1,1,1
    Carousel:
        id: caraousel
        on_current_slide: app.current_slide(self.index)
        MDFloatLayout:
            Image:
                source: "img/Hub1.jpg"
                pos_hint: {"center_x": .5, "center_y": .7}  
                size_hint_x: 1
                size_hint_y: 0.7
            MDLabel:
                pos_hint: {"center_y": .087}
                halign: "center"
                font_name: "Poppins-Light"
                font_size: "150sp"
                color: rgba(135, 143, 158, 200)    
        MDFloatLayout:
            Image:
                source: "img/Hub2.jpg"
                pos_hint: {"center_x": .5, "center_y": .7}  
                size_hint_x: 1
                size_hint_y: 0.7
            MDLabel:
                pos_hint: {"center_y": .087}
                halign: "center"
                font_name: "Poppins-Light"
                font_size: "14sp"
                color: rgba(135, 143, 158, 200)    
        MDFloatLayout:
            Image:
                source: "img/Hub3.jpg"
                pos_hint: {"center_x": .5, "center_y": .7} 
                size_hint_x: 1
                size_hint_y: 0.7
            MDLabel:
                pos_hint: {"center_y": .087}
                halign: "center"
                font_name: "Poppins-Light"
                font_size: "14sp"
                color: rgba(135, 143, 158, 200)
        MDFloatLayout:
            Image:
                source: "img/Hub5.jpg"
                pos_hint: {"center_x": .5, "center_y": .7}  
                size_hint_x: 1
                size_hint_y: 0.7
            MDLabel:
                pos_hint: {"center_y": .47}
                halign: "center"
                font_name: "Poppins-Regular"
                font_size: "25px"
                color: rgba(1, 3, 23, 225)

    
    MDBoxLayout:  
        MDFloatLayout:
            MDIcon:
                icon: 'ray-start-vertex-end'
                font_size: '40dp'
                pos_hint: {'center_x': .5, 'center_y': .32}
            MDFillRoundFlatButton:
                md_bg_color: "#49C388"
                text: "Entrar"
                font_size:17
                text_color:1,1,1,1
                pos_hint: {'center_x': .5, 'center_y': .26}
                size_hint_x: .7

                on_release: app.root.current = 'login'
            
            MDFillRoundFlatButton:
                md_bg_color: "#49C388"
                text: "Faça já o seu cadastro aqui !!"
                font_size:17
                text_color:1,1,1,1
                pos_hint: {'center_x': .5, 'center_y': .17}
                size_hint_x: .7

                on_release: app.root.current = 'whoAreyou'

            Image:  
                source: 'img/logosemnome.png'
                pos_hint: {'center_x': .5, 'center_y': .07}
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
                source: 'img/HubMat.png'
                pos_hint: {'center_x': .5, 'center_y': .7}
                size_hint_max: 250, 250
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                mode: "fill"
                fill_color_normal: 'white'
                line_color_focus: "black"
                icon_right: 'email'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                size_hint_x: .8
                hint_text: 'E-mail'
                hint_text_color_focus: "49C388"
                pos_hint: {'center_x': .5, 'center_y': .4}
            MDTextField:
                md_bg_color: "000000"
                mode: "fill"
                fill_color_normal: 'white'
                line_color_focus: "black"
                text_color_focus: "black"
                icon_right_color_focus: "49C388"
                icon_right: 'lock'
                icon_right_color_normal: "black"
                password: True
                size_hint_x: .8
                hint_text: 'Senha'
                hint_text_color_focus: "49C388"
                pos_hint: {'center_x': .5, 'center_y': .3}
            MDTextButton:
                pos_hint: {'center_x': .5, 'center_y': .22}
                text: 'Esqueceu sua senha?'  
                text_color: "white"
                theme_text_color: "Custom"
            MDFillRoundFlatButton:
                md_bg_color: "145C3A"
                text: "Entrar"
                text_color: "white"
                font_size:14
                pos_hint: {'center_x': .8, 'center_y': .17}
                size_hint_x: .1 

                on_release: app.root.current = "filter"

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
                source: 'img/MatchMilhoes.png'
                pos_hint: {'center_x': .5, 'center_y': .7}
                size_hint_max: 250, 250
            MDBoxLayout:  
            
            MDLabel:
                text: "Quem é você?"
                halign:'center'
                pos_hint: {'center_x': .5, 'center_y': .48}
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

                on_release: app.root.current = 'register_startup'

            MDFillRoundFlatButton:
                md_bg_color: "000000"
                opacity: 0.73
                text: "Investidor"
                font_size:18
                text_color:1,1,1,1
                pos_hint: {'center_x': .5, 'center_y': .3}
                size_hint_x: .7   
                
                on_release: app.root.current = 'register_investidor' 
            MDFillRoundFlatButton:
                md_bg_color: "000000"
                opacity: 0.73
                text: "Mentor"
                font_size:18
                text_color:1,1,1,1
                pos_hint: {'center_x': .5, 'center_y': .2}
                size_hint_x: .7 
                
                on_release: app.root.current = 'register_mentor'
            MDFillRoundFlatButton:
                md_bg_color: "000000"
                opacity: 0.73
                text: "Cientista"
                text_color: "black"
                font_size:18
                text_color:1,1,1,1
                pos_hint: {'center_x': .5, 'center_y': .1}
                size_hint_x: .7     
                
                on_release: app.root.current = 'register_cientista' 
                
<Register_Startup>:
    name: 'register_startup'
    MDBoxLayout:
        orientation: 'vertical'        
        MDFloatLayout:
            MDIconButton:
                icon: "chevron-left"
                user_font_size: "35sp"
                pos_hint: {"center_y": .95}
                on_release: app.root.current = 'whoAreyou'
            Image:  
                source: 'img/LogoPrincipal.png'
                pos_hint: {'center_x': .5, 'center_y': .83}
                size_hint: .4, .4
            MDLabel:
                text: "Startup"
                halign:'center'
                pos_hint: {'center_x': .5, 'center_y': .7}
                text_color: "white"
            MDTextField:  
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                mode: "fill"
                line_color_focus: "black"
                icon_right: 'email'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                hint_text_color_focus: "49C388"
                size_hint_x: .9
                hint_text: 'E-mail'
                pos_hint: {'center_x': .5, 'center_y': .6}    
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                mode: "fill"
                line_color_focus: "black"
                icon_right: 'key-variant'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                hint_text_color_focus: "49C388"
                size_hint_x: .9
                hint_text: 'Senha'
                pos_hint: {'center_x': .5, 'center_y': .45}
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                mode: "fill"
                line_color_focus: "black"
                icon_right: 'phone'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                hint_text_color_focus: "49C388" 
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

<Register_Investidor>:
    name: 'register_investidor'
    MDBoxLayout:
        orientation: 'vertical'        
        MDFloatLayout:
            MDIconButton:
                icon: "chevron-left"
                user_font_size: "35sp"
                pos_hint: {"center_y": .95}
                on_release: app.root.current = 'whoAreyou'
            Image:  
                source: 'img/LogoPrincipal.png'
                pos_hint: {'center_x': .5, 'center_y': .83}
                size_hint: .4, .4
            MDLabel:
                text: "Investidor"
                halign:'center'
                pos_hint: {'center_x': .5, 'center_y': .7}
                text_color: "white"
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                mode: "fill"
                line_color_focus: "black"
                icon_right: 'email'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                hint_text_color_focus: "49C388"
                size_hint_x: .9
                hint_text: 'E-mail'
                pos_hint: {'center_x': .5, 'center_y': .6}   
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                mode: "fill"
                line_color_focus: "black"
                icon_right: 'key-variant'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                hint_text_color_focus: "49C388"
                size_hint_x: .9
                hint_text: 'Senha'
                pos_hint: {'center_x': .5, 'center_y': .45}
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                mode: "fill"
                line_color_focus: "black"
                icon_right: 'phone'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                hint_text_color_focus: "49C388" 
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

<Register_Mentor>:
    name: 'register_mentor'
    MDBoxLayout:
        orientation: 'vertical'        
        MDFloatLayout:
            MDIconButton:
                icon: "chevron-left"
                user_font_size: "35sp"
                pos_hint: {"center_y": .95}
                on_release: app.root.current = 'whoAreyou'
            Image:  
                source: 'img/LogoPrincipal.png'
                pos_hint: {'center_x': .5, 'center_y': .83}
                size_hint: .4, .4
            MDLabel:
                text: "Mentor"
                halign:'center'
                pos_hint: {'center_x': .5, 'center_y': .7}
                text_color: "white"
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                mode: "fill"
                line_color_focus: "black"
                icon_right: 'email'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                hint_text_color_focus: "49C388"
                size_hint_x: .9
                hint_text: 'E-mail'
                pos_hint: {'center_x': .5, 'center_y': .6}   
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                mode: "fill"
                line_color_focus: "black"
                icon_right: 'key-variant'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                hint_text_color_focus: "49C388"
                size_hint_x: .9
                hint_text: 'Senha'
                pos_hint: {'center_x': .5, 'center_y': .45}
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                mode: "fill"
                line_color_focus: "black"
                icon_right: 'phone'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                hint_text_color_focus: "49C388" 
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

<Register_Cientista>:
    name: 'register_cientista'
    MDBoxLayout:
        orientation: 'vertical'        
        MDFloatLayout:
            MDIconButton:
                icon: "chevron-left"
                user_font_size: "35sp"
                pos_hint: {"center_y": .95}
                on_release: app.root.current = 'whoAreyou'
            Image:  
                source: 'img/LogoPrincipal.png'
                pos_hint: {'center_x': .5, 'center_y': .83}
                size_hint: .4, .4
            MDLabel:
                text: "Cientista"
                halign:'center'
                pos_hint: {'center_x': .5, 'center_y': .7}
                text_color: "white"
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                mode: "fill"
                line_color_focus: "black"
                icon_right: 'email'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                hint_text_color_focus: "49C388"
                size_hint_x: .9
                hint_text: 'E-mail'
                pos_hint: {'center_x': .5, 'center_y': .6}   
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                mode: "fill"
                line_color_focus: "black"
                icon_right: 'key-variant'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                hint_text_color_focus: "49C388"
                size_hint_x: .9
                hint_text: 'Senha'
                pos_hint: {'center_x': .5, 'center_y': .45}
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                mode: "fill"
                line_color_focus: "black"
                icon_right: 'phone'
                icon_right_color_normal: "black"
                icon_right_color_focus: "49C388"
                hint_text_color_focus: "49C388" 
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
                on_release: app.root.current = 'register_startup'
            Image:  
                source: 'img/LogoSemNome.png'
                pos_hint: {'center_x': .5, 'center_y': .9}
                size_hint: .2, .2
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                line_color_focus: "black"
                hint_text_color_focus: "49C388"
                size_hint_x: .4
                hint_text: "Nome"
                fill_color: 0, 0, 0, .4
                multiline: True
                pos_hint: {"center_x": .7, "center_y": .75}
            Image:  
                source: 'img/Ellipse2.png'
                pos_hint: {'center_x': .2, 'center_y': .75} 
            MDIconButton:
                icon: "upload"
                pos_hint: {'center_x': .2, 'center_y': .7} 
                user_font_size: "35sp"    
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                line_color_focus: "black"
                hint_text_color_focus: "49C388"
                
                size_hint_x: .4
                hint_text: "Seguimento"
                mode: "round"
                fill_color: 0, 0, 0, .4
                multiline: True
                pos_hint: {"center_x": .7, "center_y": .68}
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                line_color_focus: "black"
                hint_text_color_focus: "49C388"


                size_hint_x: .8
                hint_text: "Propósito"
                mode: "fill"
                fill_color: 0, 0, 0, .4
                multiline: True
                pos_hint: {"center_x": .5, "center_y": .58}
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                line_color_focus: "black"
                hint_text_color_focus: "49C388"
                
                size_hint_x: .8
                hint_text: "Vídeo pitch url"
                mode: "fill"
                fill_color: 0, 0, 0, .4
                multiline: True
                pos_hint: {"center_x": .5, "center_y": .48}
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                line_color_focus: "black"
                hint_text_color_focus: "49C388"
                

                size_hint_x: .8
                hint_text: "Pdf pitch url"
                mode: "fill"
                fill_color: 0, 0, 0, .4
                multiline: True
                pos_hint: {"center_x": .5, "center_y": .38}    
            MDTextField:
                md_bg_color: "000000"
                hint_text: "line_color_normal"
                text_color_focus: "black"
                line_color_focus: "black"
                hint_text_color_focus: "49C388"


                size_hint_x: .8
                hint_text: "#Tags"
                mode: "fill"
                fill_color: 0, 0, 0, .4
                multiline: True
                pos_hint: {"center_x": .5, "center_y": .28}             
            MDFillRoundFlatButton:
                md_bg_color: "1F4935"
                opacity: 1
                text: "Concluir"
                text_color: "black"
                font_size:14
                text_color:1,1,1,1
                pos_hint: {'center_x': .8, 'center_y': .18}
                
                on_release: app.root.current = 'login'


<Perfil>:
    name: 'perfil'
    MDBoxLayout:
        orientation: 'vertical'
       
        MDTopAppBar:
            size_hint: 1, .11
            elevation: 0
            md_bg_color: "49C388"
            anchor_title: "right"

            left_action_items: [["cog", lambda x: app.settingss_press()]]

        MDFloatLayout:
            Image:  
                source: 'img/Ellipse2.png'
                pos_hint: {'center_x': .5, 'center_y': .86}

            MDIconButton:
                icon: "pencil-outline"
                pos_hint: {"center_x": .67, 'center_y': .78}    
                size_hint: .09, .05


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


<Explorer>:
    name: 'explorer'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            size_hint: 1, .1
            elevation: 0
            md_bg_color: "49C388"
            anchor_title: "left"
            right_action_items: [["bell-outline"]]
        
        MDFloatLayout:

            MDCard:
                id: 'Azul'
                elevation: 0
                md_bg_color:  0,0,0,0
                spacing: 15
                padding: 15
                size_hint: 0.50, 0.25
                pos_hint: {'center_x': .2,'center_y': 0.50}
                MDCard:
                    id: ''
                    elevation: 0
                    md_bg_color: 
                    Image:
                        source: "img/Ellipse2.png"
                        elevation: 0


            MDCard:
                id: 'Azul'
                elevation: 0
                md_bg_color:  0,0,0,0
                spacing: 15
                padding: 15
                size_hint: 0.17, 0.15
                pos_hint: {'center_x': .2,'center_y': 0.23}
                MDCard:
                    id: ''
                    elevation: 0
                    md_bg_color: 
                    ripple_behavior: True
                    Image:
                        source: "img/VectorX.png"
                        elevation: 0
            MDCard:
                id: 'Azul'
                elevation: 0
                md_bg_color:  0,0,0,0
                spacing: 10
                padding: 10
                size_hint: 0.25, 0.15
                pos_hint: {'center_x': .8,'center_y': 0.23}
                MDCard:
                    id: ''
                    elevation: 0
                    md_bg_color: 
                    ripple_behavior: True
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
                

<Settingss>:
    name: 'settings'
    MDBoxLayout:
        orientation: 'vertical'
       
        MDTopAppBar:
            size_hint: 1, .11
            elevation: 0
            md_bg_color: "1111111"
            anchor_title: "right"
            title: "Ajustes"
            specific_text_color: "black"
        MDFloatLayout:
            MDTextField:              
                hint_text: "Pesquisar"
                mode: "round"
                icon_left: "magnify"
                pos_hint: {'center_x': .5,'center_y': .96}
                size_hint: 0.70, 0.07
            MDCard:
                elevation: 0
                md_bg_color:  0,0,0,0
                spacing: 15
                padding: 17
                size_hint: 1, 0.12
                pos_hint: {'center_x': .5,'center_y': .89 }
                
                MDCard:
                    elevation: 0
                    ripple_behavior: True
                    MDLabel:
                        adaptive_size: True
                        text: 'Notificações'
            MDCard:
                elevation: 0
                md_bg_color:  0,0,0,0
                spacing: 15
                padding: 17
                size_hint: 1, 0.12
                pos_hint: {'center_x': .5,'center_y': .81}
                
                MDCard:
                    elevation: 0
                    ripple_behavior: True
                    MDLabel:
                        adaptive_size: True
                        text: 'Privacidade'
            MDCard:
                elevation: 0
                md_bg_color:  0,0,0,0
                spacing: 15
                padding: 17
                size_hint: 1, 0.12
                pos_hint: {'center_x': .5,'center_y': .73}
                
                MDCard:
                    elevation: 0
                    ripple_behavior: True
                    MDLabel:
                        adaptive_size: True
                        text: 'Segurança'                                     
            MDCard:
                elevation: 0
                md_bg_color:  0,0,0,0
                spacing: 15
                padding: 17
                size_hint: 1, 0.12
                pos_hint: {'center_x': .5,'center_y': .65}
                
                MDCard:
                    elevation: 0
                    ripple_behavior: True
                    MDLabel:
                        adaptive_size: True
                        text: 'Anúncios'     
            MDCard:
                elevation: 0
                md_bg_color:  0,0,0,0
                spacing: 15
                padding: 17
                size_hint: 1, 0.12
                pos_hint: {'center_x': .5,'center_y': .57}
                
                MDCard:
                    elevation: 0
                    ripple_behavior: True
                    MDLabel:
                        adaptive_size: True
                        text: 'Conta'                           
            MDFloatLayout:
                Image:
                    size_hint: 1, 0.01
                    source: "img/line.png"
                    pos_hint: {'center_x': .5,'center_y': .5}
                Image:
                    size_hint: 0.65, 0.33  
                    source: "img/fada.png"
                    pos_hint: {'center_x': .5,'center_y': .3}


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
           
                    

<Chat>:
    name: 'chat'
    MDBoxLayout:
        orientation: 'vertical'
        MDFloatLayout:

            MDTextField:              
                hint_text: "Pesquisar"
                mode: "round"
                icon_left: "magnify"
                pos_hint: {'center_x': .5,'center_y': .85}
                size_hint: 0.80, 0.07

            Image:
                source: 'img/logosemnome.png'    
                pos_hint: {'center_x': .9, 'center_y': .94}
                size_hint: 0.1, 0.07
            Image:  
                source: 'img/Ellipse2.png'
                pos_hint: {'center_x': .12, 'center_y': .70}
                size_hint: 0.2, 0.1


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

<Filter>:
    name: 'filter'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            size_hint: 1, .1
            elevation: 0
            md_bg_color: "49C388"
            anchor_title: "left"
            right_action_items: [["bell-outline"]]
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


        return self.janela_gerenciadora
    
MyApp().run()
