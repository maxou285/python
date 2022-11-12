
from os.path import abspath


from kivy.app import \
    App  # Structuer de bas de kivy 1 class App 1 class MainWidget ou layout et .run
from kivy.metrics import dp
from kivy.properties import BooleanProperty, StringProperty, ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from navigation_screen_manager import NavigationScreenManager
from canvas_exemples import *       # pour tout importer

# Petite explication: Dans le fichier kv on ne peut pas utiliser de variables "normales" pour ca on doit transformer la variable en Property 
# par exemple StringProperty et comme ca on pourra utiliser la variable dans le fichier kv


class MyScreenManager(NavigationScreenManager):
    pass


class LeLabApp(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        #return CanvasExemple7()

LeLabApp().run()