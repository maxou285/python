import kivy
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.factory import Factory
from kivy.core.window import Window

Builder.load_string('''
<ScrollView>:
    size_hint: 1,1
    DrawingSpace:
        size_hint: 1,None
        height: 500
''')

class Main(App):
    def build(self):
        self.root=ScrollView()
        return self.root

class DrawingSpace(RelativeLayout):
    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        self.add_widget( Button(text = 'Scroll', size_hint=(None,None), size=(50,200), pos = (100, 100)))
        self.add_widget( Button(text = 'Scroll', size_hint=(None,None), size=(50,200), pos = (250, 300)))

Factory.register('DrawingSpace', cls=DrawingSpace)

if __name__ in ('__main__'):
    Window.size = (200, 200)
    app = Main()
    app.run()