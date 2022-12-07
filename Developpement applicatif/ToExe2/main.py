# Imports
import random
import sqlite3
import time

import pyperclip
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.button import (MDFillRoundFlatButton,
                               MDRectangleFlatIconButton,
                               MDRoundFlatIconButton,
                               MDRaisedButton,
                               MDTextButton)
from kivymd.effects.fadingedge.fadingedge import FadingEdgeEffect
from kivy.core.window import Window
# Constantes
ALPHABET_MIN = [ chr(i) for i in range(97,123) ]
ALPHABET_MAJ = [ chr(i) for i in range(65,91) ]
CHIFFRES = [ chr(i) for i in range(48,58) ]
CARACTERES_SPECIAUX = [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@']

# Create database if doesn't already exists
try:
    connexion = sqlite3.connect("base.db")
    curseur = connexion.cursor()

    curseur.execute("CREATE TABLE owner (nom_owner VARCHAR PRIMARY KEY, password_owner VARCHAR);")
    #curseur.execute("CREATE TABLE passwords (site_nom VARCHAR PRIMARY KEY,password VARCHAR,owner VARCHAR ,owner_id  INTEGER REFERENCES owner_id);")
    curseur.execute("CREATE TABLE passwords (site_nom VARCHAR ,password VARCHAR,owner VARCHAR ,owner_id  INTEGER REFERENCES owner_id, PRIMARY KEY(site_nom, owner_id));")
except:      
    pass

# Screen Manager
class NavigationScreenManager(ScreenManager):
    screen_stack = []

    def push(self, screen_name):
        if screen_name not in self.screen_stack:
            self.screen_stack.append(self.current)
            self.transition.direction = "left"
            self.current = screen_name

    def pop(self):
        if len(self.screen_stack) > 0:
            screen_name = self.screen_stack[-1]                 # -1 est le dernier élément d'une liste
            del self.screen_stack[-1]
            self.transition.direction = "right"
            self.current = screen_name


class MyScreenManager(NavigationScreenManager):
    pass
class MainWidget(BoxLayout):
    pass

class ConectionScreen(RelativeLayout):
    pass

class BoxLayout2(BoxLayout):
    def remove(self):
        print("HAS TO REMOVE         OO")
        self.remove_widget(self.Button)

class BaseMdp(RelativeLayout):
    def switch(self):
        print("switch1")
        try:
            self.ids.layout.remove_widget(self.ids.reveal_button)
        except:
            pass
        try:
            self.ids.layout.remove_widget(self.ids.cacher_button)
        except:
            pass
        button = MDTextButton(text= "\n\nCacher\n\n", pos_hint= {'center_x': 0.5})
        button.bind(on_press= lambda x: self.ids.scrollview_box.clear_widgets())
        button.bind(on_press= lambda x: self.switch2())
        self.ids['cacher_button'] = button
        self.ids.layout.add_widget(button)

    def switch2(self):
        print("switch2")
        self.ids.layout.remove_widget(self.ids.cacher_button)
        button2 = MDTextButton(text= "\n\nMontrer\n\n", on_press= lambda x: self.switch(),pos_hint= {'center_x': 0.5})
        self.ids['reveal_button'] = button2
        button2.bind(on_press= lambda x: self.ids.scrollview_box.Actualize())
        self.ids.layout.add_widget(button2)

# Define Popup
class MyPopup(Popup):
 
     
    def show_popup(self, button_text=""):
        mytext= "Que voulez vous faire ?"

        content = BoxLayout(orientation="vertical")

        content.add_widget(Label(text=mytext))

        mybutton = Button(text="Copy", size_hint=(1,.20))
        content.add_widget(mybutton)
        mybutton2 = Button(text="Delete", size_hint=(1,.20))
        content.add_widget(mybutton2)

        mypopup = Popup(content = content,              
                title = button_text,    
                auto_dismiss = True,        
                size_hint = (.7, .5),        )
        mybutton.bind(on_press=mypopup.dismiss)  
        mybutton.bind(on_press= lambda x: MyPopup().press_auth2(button_text))
        mybutton2.bind(on_press=mypopup.dismiss)  
        mybutton2.bind(on_press= lambda x:StackLayoutList.del_from_database(self, button_text))  
        mypopup.open()  
    
    def press_auth2(self, button_text):
        new_text = button_text.split(" ")
        pyperclip.copy(new_text[4])

# Define StackLayout whiwh stack passwords
class StackLayoutList(StackLayout):

    # Executer au lancement de l'application
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global site_nom
        button_list = []
        connexion = sqlite3.connect("base.db")
        curseur = connexion.cursor()
        try:
            for site_nom, password, owner, owner_id in curseur.execute('SELECT * FROM passwords where owner_id = ?', (PasswordApp.return_infos(self),)):     
                b = MDRectangleFlatIconButton(text= "" +str(site_nom) + ": \nMot de passe: " + str("".join(password)) + " \nIdentifiant: " + str(owner), halign="left", size_hint=(1, None), icon="form-textbox-password")
                b.bind(on_press=self.press_auth)
                b.btn_txt = b.text
                self.add_widget(b)
                button_list.append(b.text)
        except:
            pass
        connexion.commit()
        connexion.close()
    
    # Recupère et afficher la liste de mots de passe correspondants à la personne connectée
    def StackLayoutActualize(self, owner_name):
        connexion = sqlite3.connect("base.db")
        curseur = connexion.cursor()
        self.clear_widgets()
        for site_nom, password, owner, owner_id in curseur.execute('SELECT * FROM passwords where owner_id = ?', (owner_name,)):     
                b = MDRectangleFlatIconButton(text= "" +str(site_nom) + ": \nMot de passe: " + str("".join(password)) + " \nIdentifiant: " + str(owner), halign="left", size_hint=(1, None), icon="form-textbox-password")
                b.bind(on_press=self.press_auth)
                b.btn_txt = b.text
                StackLayoutList.add_widget(self,b)
        connexion.commit()
        connexion.close()

    # Gère le bouton montrer/cacher en affichant et supprimants les widgets dans la scrollview
    def Actualize(self):
        self.StackLayoutActualize(ident)

    # Récupère l'instance du bouton cliqué
    def press_auth(self, instance):
        return MyPopup.show_popup(self,instance.text)

    # Delete un mot de passe de la database et l'afficher à l'écran
    def del_from_database(self,text, *args):
        connexion = sqlite3.connect("base.db")
        curseur = connexion.cursor()
        text_site_split = text.split(":")
        curseur.execute('DELETE FROM passwords WHERE site_nom = ?', (text_site_split[0], ))
        connexion.commit()
        StackLayoutList.clear_widgets(self)
        for site_nom, password, owner, owner_id in curseur.execute('SELECT * FROM passwords where owner_id = ?', (PasswordApp.return_infos(self),)):   
            b = MDRectangleFlatIconButton(text= "" +str(site_nom) + ": \nMot de passe: " + str("".join(password)) + " \nIdentifiant: " + str(owner), halign="left", size_hint=(1, None), icon="form-textbox-password")
            b.bind(on_press=self.press_auth)
            b.btn_txt = b.text
            self.add_widget(b)
        curseur.close()

    # Ajouter un nouveau mot de passe dans la database et l'afficher à l'écran
    def add_new_password(self, password, site, owner, owner_id):              
        connexion = sqlite3.connect("base.db")
        curseur = connexion.cursor()
        StackLayoutList.clear_widgets(self)
        try:
            curseur.execute('INSERT INTO passwords (site_nom, password,owner, owner_id) values(?,?,?,?)', (site,password,owner, PasswordApp.return_infos(self))) #self.manager.get_screen("home_screen").ids.text_input.text, MyScreenManager().get_screen("ConnectionScreen").ids.id_create_account_identifiant.text
        except: 
            popup_warning = Popup(content = Label(text="Un autre mot de passe à déja été enregistré pour ce site"),              
                title = "Warning",    
                auto_dismiss = True,        
                size_hint = (.5, .3))
            popup_warning.open()  
        StackLayoutList.clear_widgets(self)
        for site_nom, password, owner, owner_id in curseur.execute('SELECT * FROM passwords where owner_id = ?', (PasswordApp.return_infos(self),)):
            b = MDRectangleFlatIconButton(text= "" +str(site_nom) + ": \nMot de passe: " + str("".join(password)) + " \nIdentifiant: " + str(owner), halign="left", size_hint=(1, None), icon="form-textbox-password")
            b.bind(on_press=self.press_auth)
            b.btn_txt = b.text
            self.add_widget(b)
        self.parent.parent.parent.parent.switch()
        connexion.commit()
        connexion.close()


# Classe App
class PasswordApp(MDApp):
    generate_text = StringProperty("")
    nb_cara_selection = StringProperty("")
    username = StringProperty("")
    mot_de_passe_login = StringProperty("")
    btn = ObjectProperty(None)
    create_account_identifiant = StringProperty("")
    create_account_mdp = StringProperty("")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.manager = MyScreenManager()
        return self.manager
    
    # Renvoi l'identifiant entré pas l'utilisateur dans le login
    def return_infos(self):
        return ident
 
    # Gère la connexion d'un utilisateur et rend global l'identifiant de l'utilisateur
    def login(self, identifiant, mdp):
        global ident
        ident = identifiant
        print("Trying to connect with identifiant:",identifiant, "mdp:",mdp)
        connexion = sqlite3.connect("base.db")
        curseur = connexion.cursor()
        #curseur.execute('SELECT * FROM owner where nom_owner = ?', (identifiant,))
        for nom_owner, password_owner in curseur.execute('SELECT * FROM owner where nom_owner = ?', (identifiant,)):
            print("Identifiant : " + nom_owner + " Password : " + password_owner)
            if mdp == password_owner:
                print("Password correct")
                self.manager.push("GenerateScreen")
            else:
                warn_popup = Popup(content = Label(text="ERREUR : mot de passe incorrect"),              
                    title = "Warning",    
                    auto_dismiss = True,        
                    size_hint = (.7, .5),)       
                warn_popup.open()
        list_of_users = []
        for nom_owner, password_owner in curseur.execute("SELECT * FROM owner WHERE nom_owner = ?", (identifiant,)):
            print(nom_owner, password_owner+ "COMPLETE ??")
            list_of_users.append(nom_owner)
        print(list_of_users)
        if list_of_users == []:
            print("Pas de compte existnat pour cet identifiant")
            warn_popup = Popup(content = Label(text="ERREUR : Pas de compte existant pour cet identifiant"),              
                    title = "Warning",    
                    auto_dismiss = True,        
                    size_hint = (.7, .5),)       
            warn_popup.open()
        connexion.commit()
        connexion.close()

    # Gère la création d'un nouveau compte utilisateur
    def create_account(self, identifiant, mdp):
        print("Account created with Identifiant : " + identifiant + "and Mot de passe : " + mdp)
        connexion = sqlite3.connect("base.db")
        curseur = connexion.cursor()
        try:
            curseur.execute('INSERT INTO owner (nom_owner,password_owner) values(?,?)', (identifiant, mdp))
            content = BoxLayout(orientation="vertical")
            complete_popup = Popup(content = content,              
                title = "Warning",    
                auto_dismiss = True,        
                size_hint = (.7, .5),)
            
            label1 = Label(text="Votre compte a bien été crée", size_hint=(1,.20))
            content.add_widget(label1)
            button1 = MDRaisedButton(text="Se connecter", size_hint=(1,.20))
            button1.bind(on_press= lambda x: self.manager.push("ConnectionScreen"))
            button1.bind(on_press= complete_popup.dismiss)
            content.add_widget(button1)
            complete_popup.open()
        except:
            warn_popup = Popup(content = Label(text="Un compte existe déja pour cet identifiant"),              
                title = "Warning",    
                auto_dismiss = True,        
                size_hint = (.7, .5),)
            warn_popup.open()
        connexion.commit()
        connexion.close()

    # Algorythme de géneration de mot de passe
    def generate(self):
        self.generate_text = ""
        for i in range(0, int(self.nb_cara_selection)):
            randomcara = random.randint(0,3)
            if randomcara == 0:
                self.generate_text += str(ALPHABET_MAJ[random.randint(0,25)])
            elif randomcara == 1:
                self.generate_text += str(ALPHABET_MIN[random.randint(0,len(ALPHABET_MIN)-1)])
            elif randomcara == 2:
                self.generate_text += str(CHIFFRES[random.randint(0,len(CHIFFRES)-1)])
            elif randomcara == 3:
                self.generate_text += str(CARACTERES_SPECIAUX[random.randint(0,len(CARACTERES_SPECIAUX)-1)])


Window.size = (800,600)
PasswordApp().run()