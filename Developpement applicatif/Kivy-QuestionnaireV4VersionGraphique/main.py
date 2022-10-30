##############################################################################################
# Les imports de librairie
##############################################################################################
from kivy.app import App
from kivy.properties import (  NumericProperty, ObjectProperty, StringProperty, ListProperty)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager



#from kivy.config import Config
#Config.set('graphics', 'default_font', '["GrestalScriptDemoRegular-dBYX", "fonts/GrestalScriptDemoRegular-dBYX.otf"]')


#ANSWERS = ["Paris", "Rome", "Bruxelles", "Lisbonne"]

##############################################################################################
# Déclaration des classes des différentes questions
##############################################################################################
class Question1(BoxLayout):
    answer = StringProperty("Quelle est la capitale de la France ?")
    score_int = NumericProperty(0) 
class Question2(BoxLayout):
    answer = StringProperty("Quelle est la capitale de l'Italie ?")   
class Question3(BoxLayout):
    answer = StringProperty("Quelle est la capitale de la Belgique ?")  
class Question4(BoxLayout):
    answer = StringProperty("Quelle est la capitale du Portugal ?")
     
##############################################################################################
# SceenManager
##############################################################################################
class NavigationScreenManager(ScreenManager):
    screen_stack = []

    def push(self, screen_name):
        if screen_name not in self.screen_stack:
            self.screen_stack.append(self.current)
            self.transition.direction = "left"
            self.current = screen_name
            #score += 1

      
    def pop(self):
        if len(self.screen_stack) > 0:
            screen_name = self.screen_stack[-1]                 # -1 est le dernier élément d'une liste
            del self.screen_stack[-1]
            self.transition.direction = "right"
            self.current = screen_name

class MyScreenManager(NavigationScreenManager):
   pass

##############################################################################################
# Définition de la classe App
##############################################################################################
class QuestionnaireApp(App):
    manager = ObjectProperty(None)
    number = NumericProperty(0)
    list = ListProperty()
    appréciation = StringProperty()
    
       
    def build(self):
        self.manager = MyScreenManager()
        return self.manager

        
##############################################################################################
# Programme Principal
##############################################################################################

QuestionnaireApp().run()