
from kivy.app import App                          #Structuer de bas de kivy 1 class App 1 class MainWidget ou layout et .run
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
class MainWidget(Widget):
    pass

class BoxLayoutExemple(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        self.add_widget(b1)
        b2 = Button(text="B")
        self.add_widget(b2)
class LeLabApp(App):
    pass    

LeLabApp().run()