import random
import time

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.button import (MDFillRoundFlatButton, MDRaisedButton,
                               MDRectangleFlatIconButton,
                               MDRoundFlatIconButton, MDTextButton)
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from functools import partial
from kivy.clock import Clock

# La class qui gère la grille des numéros affichés

class MyGrid(GridLayout):
    
    # On génère les boutons numérotés

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.number_list = []
        self.button_list = []
        self.add_buttons()

    # Générations des boutons

    def add_buttons(self):
        #for i in range(random.randint(3,10)):
        for i in range(9):
            self.button = Button(
                text = self.number(),
                #id = "3",
                #on_press = print(id)
            )
            self.add_widget(self.button)
            self.button_list.append(self.button)
        print(self.number_list)
        print(self.button_list)
        Clock.schedule_once(self.remove_numbers, 5)
        
    def remove_numbers(self, *largs):
        for button in self.button_list:
            button.text = ""


    # Génère aléatoirement les numéros en s'assurant qu'ils n'apparaissent chacun qu'une seule fois

    def number(self):
        button_text = random.randint(1,9)
        while button_text in self.number_list:
            button_text = random.randint(1,9)
        self.number_list.append(button_text)
        return str(button_text)
    



class MainWidget(Widget):
    pass

class BrainTrainingApp(MDApp):
    label_texte = StringProperty("")
    counter = 0
    nbmaximum = ""
    text_input_text = StringProperty("")
    reponse = ""
    same = False
    

    def build(self):
        self.theme_cls.theme_style = "Dark"
        

    def nbr_generator(self,ronde,nbmax):                                                # Cette fonction génère des nombres
        for i in range(0,ronde):
            """for n in range(0,nbmax):     
                Clock.schedule_once(self.nb_display, 2)                                 # Appelle la fonction toutes les 2 secondes
            for n in range(0,nbmax):
                Clock.schedule_once(self.nb_display, 2)                                 # Appelle la fonction toutes les 2 secondes"""
            Clock.schedule_interval(self.nb_display, 1.5) 
            self.nbmaximum = nbmax
            nbmax += 1
                
            
    def nb_display(self, _):                                                            # Le 2e argument est l'intervalle de temps
        self.counter += 1 
        generated_number = random.randint(0,9) 
        print("Generated number ",generated_number)
        print("label texte ", self.label_texte)
        while str(generated_number) == self.label_texte:
            generated_number = random.randint(0,9)
        """if str(generated_number) == self.label_texte:
            self.same = True
            print("SAMEEE")
        while self.same == True:
            generated_number = random.randint(0,9)
            if generated_number != self.label_texte:
                self.same = False"""
        self.label_texte = str(generated_number)                                     # Cette fonction affiche les chiffres à l'écran
        self.reponse = self.label_texte + self.reponse
        print(self.label_texte)
        if self.counter == self.nbmaximum:
            Clock.unschedule(self.nb_display)
            self.counter = 0
            
        

BrainTrainingApp().run()