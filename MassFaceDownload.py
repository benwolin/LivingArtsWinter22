from thispersondoesnotexist import get_online_person, save_picture
from thispersondoesnotexist import save_picture
import time

for x in range(100):
	picture = get_online_person()
	print(x)
	save_picture(picture, "./FaceCache/face{}.jpeg".format(x))
