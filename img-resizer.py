from PIL import Image, ImageOps
from os import listdir
from os.path import isfile, join

mypath = 'C:/Users/Dan/Desktop/Pillow PIP/imgs'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

new_width = int(900)

for i in onlyfiles:

    name = i

    im = Image.open('C:/Users/Dan/Desktop/Pillow PIP/imgs/' + name)

    im = ImageOps.exif_transpose(im)

    width, height = im.size
    
    new_height = int(new_width * (height / width))

    img_new = im.resize((new_width, new_height))

    img_new.save(name, dpi=(72,72), quality=60)
