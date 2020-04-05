from PIL import Image
import sys
import os


image_folder=sys.argv[1]
output_folder=sys.argv[2]


if not os.path.exists(output_folder):
    os.makedirs(output_folder)

