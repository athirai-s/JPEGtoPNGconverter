import sys
import os
from PIL import Image

#grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
#check if new/ exists or create one
if not os.path.exists(output_folder):
	os.makedirs(output_folder)
for filename in  os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{output_folder}{clean_name}.png','png')
	print('all done!')

#loop throu' pokedex and then convert it to png
#save em to the new folder
