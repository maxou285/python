
# Import the necessary libraries

from PIL import Image

from numpy import asarray





# load the image and convert into 



img = Image.open('Sample2.png')

numpydata = asarray(img)



# data

print(numpydata)
                      
