from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

#Window.maximize

class MainWidget(Widget):
    pass

class MachinaApp(App):
    pass

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import time
from PIL import Image
from numpy import asarray


class MainWidget(Widget):
    pass




class CameraClick(BoxLayout):

    # Capturer une image, lui donner un nom en fonction de la date/heure, l'exporter en png puis la convertir en Tableau Numpy
    def capture(self):

        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        image_name = "IMG_{}.png".format(timestr)
        camera.export_to_png(image_name)
        print("Captured")
        img = Image.open(image_name)
        numpydata = asarray(img)
        print(numpydata)


class MachinaApp(App):
    pass



MachinaApp().run()



