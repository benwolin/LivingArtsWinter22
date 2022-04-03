import tkinter as tk
from PIL import Image, ImageTk
import io

class FaceDisplay:
    IM_WIDTH = 800
    IM_HEIGHT = 480
    def __init__(self, root):
        self._root = root
        self._currentImage = None
        self._imagelabel = tk.Label(self._root, image = self._currentImage, bg = "purple")

    def UpdateImage(self, imBytes: bytes):
        im = Image.open(io.BytesIO(imBytes))
        im = im.resize((self.IM_WIDTH,self.IM_HEIGHT), Image.ANTIALIAS)

        self._currentImage = ImageTk.PhotoImage(im)
        self._imagelabel.configure(image=self._currentImage)
        self._imagelabel.image=self._currentImage
        self.DisplayImage()

    def DisplayImage(self):
        self._imagelabel.pack()





