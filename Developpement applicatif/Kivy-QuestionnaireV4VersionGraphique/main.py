
from tkinter.ttk import Button

from kivy.app import *
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager

# On utilise ce fichier pour perfectionner le fonctionnement des ScreenManagers comme ca on pourra aussi simplement revenir en arrière 

answers = ["Paris", "", "", ""]

class Question1(BoxLayout):
    answer = StringProperty("Quelle est la capitale de la France ?")
    def verify_answer(self, text):
        self.answer = text
        if self.answer == answers[0]:
            print("Correct")
            self.answer = "Bravo ! "
            
            
        else:
            print("Incorrect")
            self.answer = "Mauvaise Réponse réessaie ! "

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


class QuestionnaireApp(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager




QuestionnaireApp().run()