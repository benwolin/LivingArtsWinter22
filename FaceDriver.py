import os
import tkinter as tk
from FaceDisplay import FaceDisplay
from thispersondoesnotexist import get_online_person
import time, threading


root = tk.Tk()
root.title("Face Display")
root.geometry('800x480')
root.wm_attributes('-fullscreen','true')
root.update()

fd =  FaceDisplay(root)

def ImageUpdateThread():
	while True:
		print("UPDATE IMAGE")
		picture = get_online_person()
		fd.UpdateImage(picture)
		time.sleep(5)

updateThread = threading.Thread(target = ImageUpdateThread, daemon = True )
updateThread.start()

#Start the display
root.mainloop()