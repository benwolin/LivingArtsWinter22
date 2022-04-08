import os
import tkinter as tk
from FaceDisplay import FaceDisplay
import time, threading, random 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--facetime", required = False, type=int, default = 20, help = 'The time in miliseconds between face cycles')
args = vars(ap.parse_args())
FACE_CYCLE = args['facetime']/1000

NUM_CACHED = 100
CYCLE_TIME = 6

def get_cached_face(cacheCount):
	faceFile =  "./FaceCache/face{cacheCount}.jpeg".format(cacheCount = cacheCount)
	if not os.path.exists(faceFile):
		return None, False

	with open(faceFile, 'rb') as readb:
		return readb.read(), True

def ImageUpdateThread():
	while True:
		cachedImageNum = random.randint(0, NUM_CACHED - 1)
		picture, success = get_cached_face(cachedImageNum)
		if success:
			fd.UpdateImage(picture)
		else:
			print("OH NO THIS SHOULD NOT HAPPEN:", cachedImageNum)
			
		time.sleep(FACE_CYCLE)


root = tk.Tk()
root.title("Face Display")
root.geometry('800x480')
#root.wm_attributes('-fullscreen','true')
root.update()

fd =  FaceDisplay(root)
updateThread = threading.Thread(target = ImageUpdateThread, daemon = True )
updateThread.start()

#Start the display
root.mainloop()