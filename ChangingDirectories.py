import os
import shutil

# make new folders in train for cats and dogs
os.mkdir('train/cats')
os.mkdir('train/dogs')

folder = 'train/'

for file in os.listdir(folder):
	if file.startswith('cat.'):
		shutil.move(folder + file, folder + 'cats')
    elif file.startswith('dog.'):
        shutil.move(folder + file, folder + 'dogs')
