from storage_manager import StorageManager
from http_client import HttpClient
from models import Pizza
from kivy.app import App                
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.label import Label

class PizzaWidget(BoxLayout):
    nom = StringProperty("")
    prix = NumericProperty()
    ingredients = StringProperty("")
    vegetarienne = BooleanProperty()

class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """self.pizzas = [
            Pizza("4 fromages", "chèvre, emmental, brie, comté", 9.5, True),
            Pizza("Chorizo", "tomate, chorizo, parmesan", 11.2, False),
            Pizza("Calzone", "fromage, jambon, champignon", 10, False),
        ]"""
    
        HttpClient().get_pizzas(self.on_server_data, self.on_server_error)


    def on_parent(self, widget, parent):
        #self.recycleView.data = [pizza.get_dictionnary() for pizza in self.pizzas]
        pizza_dict = StorageManager().load_data("pizzas")
        if pizza_dict != None:
            self.recycleView.data = pizza_dict

    def on_server_data(self, pizza_dict):
        self.recycleView.data = pizza_dict
        StorageManager().save_data("pizzas", pizza_dict)

    def on_server_error(self, error):
        print("Error : " + error)
        self.error_str = "Error : " + error
class PizzaApp(App):
    pass

PizzaApp().run()