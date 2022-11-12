
import kivy  
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.base import runTouchApp
from kivy.lang import Builder
 
 
# Build the .kv file
Builder.load_string('''
 
# Define the scroll view
<ScrollView>:
    text: 'You are learning Kivy' * 500
    Label:
        text: root.text
        font_size: 50
        text_size: self.width, None
        size_hint_y: None
        height: self.texture_size[1]
''')
 
 
# Define scrollview class
class ScrollableLabel(ScrollView):
    text = StringProperty('')
 
# run the App
runTouchApp(ScrollableLabel())