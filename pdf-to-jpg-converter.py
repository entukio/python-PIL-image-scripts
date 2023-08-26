from PIL import Image, ImageOps
from os import listdir
from os.path import isfile, join
from pdf2image import convert_from_path

#https://pdf2image.readthedocs.io/en/latest/reference.html?highlight=convert_from_path#pdf2image.pdf2image.convert_from_path

mypath = 'C:/Users/Dan/Desktop/Pillow PIP/imgs/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for i in onlyfiles:
    name = i
    print(mypath+i)
    img = convert_from_path(mypath+i,72,poppler_path=r'C:\Program Files\poppler-0.68.0\bin',fmt='jpeg',transparent=False)
    img[0].save(str(i)+'-t.jpg','JPEG')
