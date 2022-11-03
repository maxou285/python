#############################################################################################
# Les Imports de Librairie
#############################################################################################
from kivy.properties import (Clock, DictProperty, NumericProperty,StringProperty)
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

#############################################################################################
# Déclaration des différentes classes
######################################################################################pip list#######

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


#############################################################################################
# Déclaration de la classe App
#############################################################################################
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

#############################################################################################
# Programme Principal
#############################################################################################
Window.size = (380, 700)
IsPremierApp().run()
