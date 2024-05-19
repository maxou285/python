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
    
    def picture_taken(self,instance):
        print("Got the picture")
        camera = instance.parent.ids.xcamera
        timestr = time.strftime("%Y%m%d_%H%M%S")
        #timestr= time.strftime("%Y%-%m%-%d_%H%M%S")
        image_name = "IMG_{}.png".format(timestr)
        camera.export_to_png(image_name)
        print("Captured")
        img = Image.open(image_name)
        numpydata = asarray(img)
        print(numpydata)


    def change_cam(self, instance):
        camera = instance.parent.ids.xcamera
        if camera.index == 0:
            camera.index = int(camera.index) + 1    
        elif camera.index == 1:
            camera.index = int(camera.index) - 1  
        else:
            camera.index = camera.index

Main().run()  
