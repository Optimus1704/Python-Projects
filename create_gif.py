# Final project with Python

# Create a GIF with Python


# GIF with two images

# In this case I didn't have any issue in using the two images

import imageio.v3 as iio
from PIL import Image
import numpy as np 

filenames = ['chicklet1.png', 'chicklet2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('chicklet.gif', images, duration = 500, loop = 0) # I put the duration to 500 because I believe it's the proper number to maintain a constant movement between the two images


# GIF with three images

# I had to use PIL and numpy in order to work with the three images, the reason is that VSCode in any situation stated that the three images have to be the same size, even if the images have the same measures when I looked at their properties

filenames = ['nyan-cat1.png', 'nyan-cat2.png','nyan-cat3.png']
images = [ ]

first_size = None  

for filename in filenames:
    img = iio.imread(filename)
    
    pil_img = Image.fromarray(img)
    
    pil_img = pil_img.convert('RGBA')
    
    if first_size is None:
        first_size = pil_img.size  
    
    pil_img = pil_img.resize(first_size) 
    
    images.append(np.array(pil_img))

iio.imwrite('nyan_cat.gif', images, duration = 300, loop = 0) # I put the duration to 300 because I believe it's the proper number to maintain a constant movement between the three images
