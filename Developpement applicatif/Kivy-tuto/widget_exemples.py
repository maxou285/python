from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.lang import Builder

Builder.load_file("widget_exemples.kv")


class WidgetsExemple(GridLayout):
    mon_texte = StringProperty("Bonjour")          # StringProperty est pour créer une propriété ici ca permet de modifier le texte du label
    text_input_str = StringProperty("toto")
    # slider_value_txt = StringProperty("50")
    compteur = 0
    compteur_actif = BooleanProperty(False)
    def on_button_click(self):
        if self.compteur_actif == True:
            self.compteur += 1
            print("Button click")
            self.mon_texte = str(self.compteur)
    
    def on_button_toggle_state(self, widget):
        #print("ToggleState " + widget.state)
        if widget.state == "normal":
            print("OFF")
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            print("ON")
            widget.text = "ON"
            self.compteur_actif = True
    
    def on_switch_active(self, widget):
        print("Switch : " + str(widget.active))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text

    #def on_slider_value(self, widget):
    #   print("Slider : " + str(int(widget.value)))
        #self.slider_value_txt = str(int(widget.value))