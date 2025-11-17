# Final project with Python

# Create a GIF with Python


# GIF with two images

# In this case I didn't have any issues using the two images

import imageio.v3 as iio

filenames = ['chicklet1.png', 'chicklet2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('chicklet.gif', images, duration = 500, loop = 0) 

# I set the duration to 500 milliseconds because 
# I believe it's the right value to maintain a smooth transition between the two images
