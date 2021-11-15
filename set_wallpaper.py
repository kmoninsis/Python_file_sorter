import time
import ctypes
import os
import sys

localtime = time.localtime(time.time())
path = "C:/Users/Simon/Documents/Python scripts/wallpaper/"
files = os.listdir(path)
imgs = []

print(localtime.time.gmtime(tm_hour))
# for f in files:
# 	imgs.append(os.path.abspath(os.path.join(path, f)))
	
# try:
# if localtime.gmtime(tm_hour) > 20:
# 	ctypes.windll.user32.SystemParametersInfoW(20, 0, imgs[0], 0)
# 	print("It's after 20:00. Desktop change was succesfull")
# else:
# 	ctypes.windll.user32.SystemParametersInfoW(20, 0, imgs[1], 0)
	# print("It's before 20:00. Desktop change was succesfull")
# except:
# 	print("Unexpected error:", sys.exc_info()[0])