from os.path import curdir

from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import sp
from kivy.properties import (Clock, DictProperty, NumericProperty,
                             StringProperty)
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivymd.app import MDApp


# Tout le code en commentaire revient au meme mais sans le fichier kv c'est la 2e facon de faire avec kivy si on ne veut pas utiliser le fichier kv
# mais avec cette facon il faut utiliser la fonction build dans la classe App
"""
            size_hint: (None, None)
            pos: root.width*0.4,root.height*0.1
            height: root.height*0.1
            width: root.width*0.23
            text: app.text_input

KV = '''
MDBoxLayout:
    
    orientation: "vertical"

    MDTopAppBar:
        title: "MDTopAppBar"
    Widget:
        TextInput:
            id: input
            size_hint: (None, None)
            pos: root.width*0.4,root.height*0.3
            height: root.height*0.04
            width: root.width*0.23
            multiline: False
            text: "Rentrez un nombre"
            on_double_tap: self.text = ""

        Button:
            text: "Voir Résultats"
            pos: root.width*0.4,root.height*0.22
            size_hint: None, None
            height: root.height*0.05
            width: root.width*0.23
            size: 350,70
            on_press: app.is_premier(input.text)
        TextInput:
            size_hint: (None, None)
            pos: root.width*0.4,root.height*0.1
            height: root.height*0.1
            width: root.width*0.23
            text: app.text_input
            on_double_tap: self.text = ""
'''
"""
from kivy.uix.screenmanager import ScreenManager

# On utilise ce fichier pour perfectionner le fonctionnement des ScreenManagers comme ca on pourra aussi simplement revenir en arrière 


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
# To explain briefly IsPremier is a little project of mine\n                       made with the kivy python module. The user have to enter a number in the field\n                and click on the button.Then the app will tell him if the number is a prime number or not"
class MainWidget(Widget):
    pass

class IsPremierApp(MDApp):
    text_input = StringProperty("Rentrez un nombre")
    text_answer = StringProperty("Réponses : ")
    data = DictProperty()
    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        #return Builder.load_string(KV)
    def is_premier(self, nbr):

        try:    
            nbr = int(nbr)
            if nbr > 0:
                test = True
                for i in range(2, int(nbr)):
                    if (nbr % i) == 0:
                        print("Ce nombre n'est pas premier")
                        self.text_input = "Pas premier\nDivisible par : " + str(i)
                        test = False
                        break
                if test == True:
                    print("Ce nombre est premier")
                    self.text_input = "Premier"
        except:
            self.text_input = "Rentrez un nombre correct"

    def call(self):
        print("Called")

IsPremierApp().run()
