import os, time, shutil, sys
from PIL import Image

def get_date_taken(path):
	ftime = Image.open(path)._getexif()[36867]
	splitted = ftime.split(':')
	dateyear = splitted[0]
	datemonth = splitted[1]
	ctime_dir = dateyear + '-' + datemonth
	return ctime_dir

def get_date_modified(path):
	ftime = time.gmtime(os.path.getmtime(f))
	return time.strftime("%Y-%m", ftime)

def get_dates(path):
	try:
		return get_date_taken(path)
			
	except:
		return get_date_modified(path)
		print("No Exif data available")


dir = "E:/2016/Telefoon fotos"
os.chdir(dir)
for f in os.listdir('.'):
	path = dir + '/' + f	
	ctime_dir = get_dates(path)
	dstdir = ctime_dir + '/' + f
	if f.endswith('.py') is True:
		print(".... Skipped .py file")
		continue
	elif os.path.isdir(f) is True:
		print(".... Skipped folder")
		continue
	elif not os.path.isdir(ctime_dir):
		os.mkdir(ctime_dir)
		print(".... Folder " + ctime_dir + " was made")
		shutil.move(f, dstdir)
		print(".... File " + f + " was moved to folder " + ctime_dir)
	else:
		print(".... Folder " + ctime_dir + " allready exists")
		if os.path.isfile(dir+'/'+dstdir) is True:
			print(".... File allready exists") 
			continue
		else:
			shutil.move(f, ctime_dir)
			print(".... File " + f + " was moved to folder " + ctime_dir)



			

		
		
				

