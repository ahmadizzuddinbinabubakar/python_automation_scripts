import PIL
from PIL import Image
from tkinter.filedialog import *

fl=askopenfilenames()
img = Image.open(fl[0])

#convert to JPG
img.save("output.jpg", "jpeg")

#convert to PNG
img.save("output.png", "png")

#convert to WEBP
img.save("output.webp", "webp")