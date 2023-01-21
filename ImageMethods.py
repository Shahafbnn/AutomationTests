import tkinter
from PIL import Image, ImageFilter

def Outline():
    image = Image.open('apple.png')
    image = image.filter(ImageFilter.FIND_EDGES)
    resized = image.copy()
    resized = resized.resize((image.width+100, image.height+100))


    width, height = resized.size
    left = (width - image.width) / 2
    top = (height - image.height) / 2
    right = (width + image.width) / 2
    bottom = (height + image.height) / 2

    resized = resized.crop((left, top, right, bottom))
    image = Image.blend(resized, image, 0.5)
    image.show()
    image.save('bruh.png')

