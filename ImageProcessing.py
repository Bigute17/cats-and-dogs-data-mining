import os
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

# Location of our images
folder = 'train/'
photos, labels = list(), list()

for file in os.listdir(folder):
	# determine the classification
	output = 0.0
	if file.startswith('dog'):
		output = 1.0
	# load the image as 300x300
	photo = load_img(folder + file, target_size=(300, 300))
	# convert it to a numpy array
	photo = img_to_array(photo)
	# store it
	photos.append(photo)
	labels.append(output)
  
 # convert to numpy arrays
photos = np.asarray(photos)
labels = np.asarray(labels)
print(photos.shape, labels.shape)
# save the reshaped photos
np.save('dogs_vs_cats_photos.npy', photos)
np.save('dogs_vs_cats_labels.npy', labels)

# DO NOT RUN THIS SCRIPT IF YOU HAVE LESS THAN 12GB of RAM
# The two files above will be created and they are simply the resized images with classifications


# load and confirm the shape
photos = np.load('dogs_vs_cats_photos.npy', allow_pickle=True)
labels = np.load('dogs_vs_cats_labels.npy', allow_pickle=True)
print(photos.shape, labels.shape)
