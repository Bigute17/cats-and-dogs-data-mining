import os
import re
from matplotlib import pyplot
from matplotlib.image import imread


# Location of the data
folder = 'train/'

# Plot some of the cat images 
for i in range(9):
	# define the subplot
	pyplot.subplot(330 + 1 + i)
	# define the filenames
	filename = folder + 'cat' + '.' + str(i) + '.jpg'
	# load the image pixels
	image = imread(filename)
	# plot raw pixel data
	pyplot.imshow(image)
 
# show the figure
pyplot.show()

# Plot some of the dog images 
for i in range(9):
	# define the subplot
	pyplot.subplot(330 + 1 + i)
	# define the filenames
	filename = folder + 'dog' + "." + str(i) + '.jpg'
	# load the image pixels
	image = imread(filename)
	# plot raw pixel data
	pyplot.imshow(image)
 
 # show the figure
pyplot.show()

# We can see that the images differ in size, this will be an issue for our predictions
# So we should try and streamline all the images to be one size.

