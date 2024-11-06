from kivy.app import App
from kivy.lang import Builder
from kivy_garden import xcamera
from PIL import Image
import time
from numpy import asarray
import numpy as np
#from rembg import remove
import cv2

class Main(App):
    def build(self):
        return Builder.load_file("machina.kv")
    

    ###### Fonction qui rotate l'image mais du coup on a des bordures noires ce qui fausse le numpyarray
    #def picture_taken(self,instance):
    #    print("Got the picture")
    #    camera = instance.parent.ids.xcamera
    #    timestr = time.strftime("%Y%m%d_%H%M%S")
    #    image_name = "IMG_{}.png".format(timestr)
    #    camera.export_to_png(image_name)
    #    img = Image.open(image_name)
    #    img = Image.open(timestr)
    #    numpydata = asarray(img)
    #    print(numpydata)


    #### Fonction qui ne rotate pas l'image mais qui récupère le numpy array parfaitement
    def picture_taken(self,instance):
        print("Got the picture")
        camera = instance.parent.ids.xcamera
        timestr = time.strftime("%Y%" + "--" + "%m%"+"--"+"%d"+ " " + "%H.%M.%S.jpg") ## exact same pattern as normal os format
        img = Image.open(timestr)
        numpydata = asarray(img)
        print(numpydata)
        new_array = np.rot90(numpydata) ### pour rotate le numpy array de 90°
        print("CHANGE")
        print(new_array)


    def change_cam(self, instance):
        camera = instance.parent.ids.xcamera
        if camera.index == 0:
            camera.index = int(camera.index) + 1    
        elif camera.index == 1:
            camera.index = int(camera.index) - 1  
        else:
            camera.index = camera.index

Main().run()  
