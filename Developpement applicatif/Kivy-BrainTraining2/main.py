from kivy.app import App
from kivy.uix.widget import Widget
import random
from kivy.properties import (  NumericProperty, ObjectProperty, StringProperty, ListProperty)
import time
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.gridlayout import GridLayout

##############################################################################################
# SceenManager
##############################################################################################
class NavigationScreenManager(ScreenManager):
    screen_stack = []

    def push(self, screen_name):
        if screen_name not in self.screen_stack:                # on ne peut pas aller vers l'écran sur lequel on est déja
            self.screen_stack.append(self.current)
            self.transition.direction = "left"
            self.current = screen_name


      
    def pop(self):
        if len(self.screen_stack) > 0:                          # vérifier qu'il y a des éléments dans screen_stack
            screen_name = self.screen_stack[-1]                 # -1 est le dernier élément d'une liste
            del self.screen_stack[-1]
            self.transition.direction = "right"
            self.current = screen_name

class MyScreenManager(NavigationScreenManager):
   pass

class QuestionScreen(GridLayout):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.number_list = []

    
    def select_random_number(self):
        nbr = random.randint(1,9)
        if nbr in self.number_list:
            return(self.select_random_number())
        else:
            print(self.number_list)
            self.number_list.append(nbr)
            return str(nbr)



##############################################################################################
# Class App
##############################################################################################
        
class BrainTraining2App(App):
    manager = ObjectProperty(None)
    
    def build(self):
        self.manager = MyScreenManager()
        return self.manager

BrainTraining2App().run()
