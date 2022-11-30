from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.image import Image
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color

class MainWidget(Widget):
    request = StringProperty("This is a previous text, don't mind")
    insert_text = StringProperty("Insert Here")
    window_size = (305,400)
    refresh_key = False
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.Window_Minimum()
    
    def on_size(self,*args):
        print(self.width,self.height)
    
    def on_text_validate(self,widget): #<<<<<<<<<<<<<<<<<<<<<<<<<<< input text
        request=widget.text
        Chat_history_update().chat_history(request)
        
    def Window_Minimum(self):
        Window.minimum_width,Window.minimum_height=self.window_size

class Chat_history_update(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        l = Label(text="This is a previous text, don't mind",size_hint=(1, None),height=("30dp"))
        self.add_widget(l)
        
    def chat_history(self,request): # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Add Label Function
        l = Label(text=request, size_hint=(1, None),height=("30dp"))
        self.add_widget(l) # <<<<<<<<<<<<< This won't update my app screen

class Assistant(App):
    pass

if __name__ == "__main__":
    Assistant().run()