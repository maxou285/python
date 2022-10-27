
############################################################################
# 1st Method need kv file
############################################################################
from kivy.app import App
from kivy.uix.widget import Widget

class MainWidget(Widget):
    pass

class QuestionnaireApp(App):
    pass


QuestionnaireApp().run()


############################################################################
# 2nd Method don't need kv file
############################################################################

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

KV_CODE = '''
#:import Window kivy.core.window.Window
BoxLayout:
<BoxLayout@BoxLayout>:
    Button:
        text: "Hey"
    Label:
        text: "RHO"
'''
class MainWidget(Widget):
    pass

class QuestionnaireApp(App):
    def build(self):
        return Builder.load_string(KV_CODE)



QuestionnaireApp().run()