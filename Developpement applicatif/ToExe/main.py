# Pour que ca fonctionne il faut selectionner le bon interpreteur python ici je suis dans venv dans le terminal et python 3.10('venv':venv)



from kivy.app import App                          #Structuer de bas de kivy 1 class App 1 class MainWidget ou layout et .run
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class MainWidget(Widget):
    pass


class StackLayoutExemple(StackLayout):
    
    
    mon_resultat = StringProperty("")          # StringProperty est pour créer une propriété ici ca permet de modifier le texte du label
    a = ""
    b = ""
    operateur = ""
    equal = False
    
    def on_button_click(self, button = "",operateur = "",  equal = False):
        
        
        
        print(self.a)
        print(self.b)
        self.mon_resultat += button
        self.b = self.mon_resultat
        global operateur2 
        try:
            if operateur == "+":
                self.a = self.mon_resultat
                self.mon_resultat = ""
                operateur2 = "+"
                    
                
            if operateur == "-":
                self.a = self.mon_resultat
                self.mon_resultat = ""
                operateur2 = "-"

            if operateur == "/":
                self.a = self.mon_resultat
                self.mon_resultat = ""
                operateur2 = "/"

            if operateur == "*":
                self.a = self.mon_resultat
                self.mon_resultat = ""
                operateur2 = "*"


            if operateur == "%":
                self.mon_resultat = str(float(self.mon_resultat) * 0.01)

            if operateur == "+/-":
                self.mon_resultat = str(float(self.mon_resultat) * -1)

            if equal == True:
                if operateur2 == "+":                          
                    self.mon_resultat = str(float(self.a) + float(self.b))
                
                if operateur2 == "-":
                    self.mon_resultat = str(float(self.a) - float(self.b))
                
                if operateur2 == "/":
                    self.mon_resultat = str(float(self.a) / float(self.b))

                if operateur2 == "*":
                    self.mon_resultat = str(float(self.a) * float(self.b))


                '''if operateur2 == "+/-":
                    if self.mon_resultat > 0:
                        self.mon_resultat = str(int(-self.a))
                    elif self.mon_resultat < 0:
                        self.mon_resultat = str()'''
            
            if button == "AC":
                self.mon_resultat = ""
        except:
            print("Vous devez rentrer un nombre correct")
            self.mon_resultat = "Vous devez rentrer un nombre correct Pressez AC"
            
           

        
            
       
       

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation = "lr-tb"
        


class CalculatriceApp(App):
    pass  


CalculatriceApp().run()




