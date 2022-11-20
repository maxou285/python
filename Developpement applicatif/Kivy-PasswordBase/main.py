import random
import sqlite3

from kivy.app import App
from kivy.graphics import Rectangle
from kivy.metrics import dp
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.stacklayout import StackLayout
from kivymd.app import MDApp
from kivymd.uix.button import (MDFillRoundFlatButton,
                               MDRectangleFlatIconButton,
                               MDRoundFlatIconButton)

ALPHABET_MIN = [ chr(i) for i in range(97,123) ]
ALPHABET_MAJ = [ chr(i) for i in range(65,91) ]
CHIFFRES = [ chr(i) for i in range(48,58) ]
CARACTERES_SPECIAUX = [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@']


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

class StackLayoutList(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global site_nom
        
        connexion = sqlite3.connect("base.db")
        curseur = connexion.cursor()
        site_nom = curseur.execute('SELECT * FROM passwords')
        for site_nom, password in curseur.execute('SELECT * FROM passwords'):
            b = MDRectangleFlatIconButton(text= "" + str(site_nom) + ": " + str("".join(password)), halign="left", size_hint=(1, None), icon="form-textbox-password")
            b.bind(on_press=self.remove_widget)
            #b.bind(on_press=lambda x: print("Deleted"))
            #print()
            b.bind(on_press= lambda x: self.del_from_database(b.text))
            self.add_widget(b)

        connexion.commit()
        connexion.close()

    def del_from_database(self,text, *args):
        connexion = sqlite3.connect("base.db")
        curseur = connexion.cursor()
        print("Connected to sqlite")
        print("Site nom : " + text)
        text_site_split = text.split(":")
        print(text_site_split)
        curseur.execute('DELETE FROM passwords WHERE site_nom = ?', (text_site_split[0], ))
        connexion.commit()
        print("Record deleted successfully ")
        curseur.close()


    def add_new_password(self, password, site):
        #global site_name_for_database
        #site_name_for_database = site
        new_password = site + ": " + password
        b1 = MDRectangleFlatIconButton(text= "" + new_password, halign="left", size_hint=(1, None), icon="form-textbox-password")
        b1.bind(on_press=self.remove_widget)
        b1.bind(on_press=lambda x: print("Deleted"))
        b1.bind(on_press= lambda x: self.del_from_database(b1.text))
        self.add_widget(b1)
                
        connexion = sqlite3.connect("base.db")
        curseur = connexion.cursor()
        curseur.execute('INSERT INTO passwords (site_nom, password) values(?,?)', (site,password))
        connexion.commit()
        connexion.close()


class PasswordApp(MDApp):
    generate_text = StringProperty("")
    nb_cara_selection = StringProperty("")


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.manager = MyScreenManager()
        return self.manager

    def generate(self):
        print("Generate asked")
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

        

PasswordApp().run()