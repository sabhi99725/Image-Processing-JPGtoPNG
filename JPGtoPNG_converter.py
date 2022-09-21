import sys
import os
from PIL import Image
# creat first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]
#creat folder if does not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
#using for loop convert jpg to png
for images in os.listdir(image_folder):
    image = Image.open(f'{image_folder}{images}')
    #remove jpg from images
    clean_name = os.path.splitext(images)[0]
    image.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')
