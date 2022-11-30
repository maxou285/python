from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class AddWindow(Screen):
    def __init__(self, **kwargs):
        super(AddWindow, self).__init__(**kwargs)

        self.grid = StackLayout()
        self.grid.pos_hint = {"x":0.05,"top":0.8}
        self.grid.size_hint = (0.9,None)
        self.add_widget(self.grid)

        self.i = 1
        self.n = 1
        self.inputs = {}
        self.ing1 = TextInput(size_hint=(0.9,'0.3sp'))
        self.grid.add_widget(self.ing1)
        self.inputs['0'] = 'ing1'

        self.addIng = Button(text="+", size_hint=(0.1,'0.3sp'))
        self.addIng.bind(on_press=self.addIngredient)
        self.grid.add_widget(self.addIng)

        self.doneButton = Button(text="Save")
        self.grid.add_widget(self.doneButton, index=0)

    def addIngredient (self, instance):
        self.ing = TextInput(size_hint=(0.9,'0.3sp'))
        self.inputs[self.i] = 'ing{}'.format(self.i+1)
        self.grid.add_widget(self.ing, index=self.n+1)

        self.addNext = Button(text="+", size_hint=(0.1,'0.3sp'))
        self.addNext.bind(on_press=self.addIngredient)
        self.grid.add_widget(self.addNext, index=self.n+2)
        self.i += 1
        self.n += 2
        print(self.inputs)        

WMan = ScreenManager() 
WMan.add_widget(AddWindow(name='add'))


class RecipApp(App):
    def build(self):
        return WMan

if __name__ == "__main__":
    RecipApp().run()