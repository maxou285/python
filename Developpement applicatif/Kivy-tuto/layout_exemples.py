from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.button import Button

Builder.load_file("layout_exemples.kv")




class MainWidget(Widget):
    pass

#class ScrollViewExemple(ScrollView):           # ces lignes ne sont pas obligatoires car on a deja importé scrollview avec la syntaxe @ScrollView dans le fichier kv
#    pass
class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation = "lr-tb"
        for i in range(0, 100):    
            b = Button(text=str(i + 1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)

#class ImagesExemple(GridLayout):
#    pass

#class GridLayoutExemple(GridLayout):
#   pass
class AnchorLayoutExemple(AnchorLayout):
    pass

class BoxLayoutExemple(BoxLayout):
    pass
    """def __init__(self, **kwargs):           # Kivy à besoin de l'argument **kwargs mais nous on ne s'en sert pas
        super().__init__(**kwargs)
        self.orientation = "vertical"       # Si les boutons vont etre affichés verticalements ou horizontalements
        b1 = Button(text="A")               # Il y a 2 facons pour afficher des boutons avec le BoxLayout 1 dans le code comme ici ou 2 dans le fichier .kv
        self.add_widget(b1)
        b2 = Button(text="B")
        self.add_widget(b2)
        b3 = Button(text="C")
        self.add_widget(b3)"""
