from kivy.lang import Builder

from kivymd.app import MDApp

"""KV = '''

MDRectangleFlatButton:
    text: "MDRectangleFlatButton"
    theme_text_color: "Custom"
    text_color: "black"
    line_color: "red"
'''"""


class Example(MDApp):
    """def build(self):
        #self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "Orange"
        #self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)"""

    '''def on_start(self):
        data = {
            "standard": {"md_bg_color": "#fefbff", "text_color": "#6851a5"},
            "small": {"md_bg_color": "#e9dff7", "text_color": "#211c29"},
            "large": {"md_bg_color": "#f8d7e3", "text_color": "#311021"},
        }
        for type_button in data.keys():
            self.root.ids.box.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type=type_button,
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    icon_color=data[type_button]["text_color"],
                )
            )'''


Example().run()