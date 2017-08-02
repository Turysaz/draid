#originalpfad ist das erste Argument, backuppfad das zweite

import os, sys, shutil
from datetime import date, timedelta

#path1 = r"/home/turysaz/Schreibtisch/orig/"
#path2 = r"/home/turysaz/Schreibtisch/bkup/"
#root_orig = path1
#root_bkup = path2
root_orig = sys.argv[1]
root_bkup = sys.argv[2]

os.stat_float_times(False)

def dateString(d = 0):

	delta = timedelta(days = d)
	this_date = date.today() + delta

	#YEAR
	_year = str(this_date.year)
	#MONTH
	_mon = str(this_date.month)
	_mon = addZeros(_mon, 2)
	#DAY
	_day = str(this_date.day)
	_day = addZeros(_day,2)

	_date = _year + _mon + _day
	
	return _date

def addZeros(i, l, symbol = "0"):
	i = str(i)
	while (len(i)<l):
		i = symbol+i
	return i

today = dateString()
monthago = dateString(-30)


def comparecur(path_o, path_b):
	list_o = os.listdir(path_o)
	list_b = os.listdir(path_b)
	
	for item_o in list_o:
		# suche neue Dateien
		if(not item_o in list_b):
			print("new file: " + ascii(path_o + item_o))
			if(os.path.isdir(path_o+item_o)):
				shutil.copytree(path_o + item_o	, path_b + item_o)	
			else:
				shutil.copy2(path_o + item_o, path_b + item_o)
		if(os.path.isdir(path_o + item_o)):
			# durchsuche unterverzeichnis
			comparecur(path_o + item_o + "/", path_b + item_o + "/" )
		else:
			if(os.path.getmtime(path_o+item_o)>os.path.getmtime(path_b+item_o)):
				print("changed: " + ascii(path_o + item_o))
				shutil.copy2(path_o+item_o, path_b+item_o)
	
	for item_b in list_b:
		if(not item_b in list_o):
			if(item_b[:3]=="DEL"):
				dod = int(item_b[3:11])
				if(dod < int(monthago)):
					print("finally deleted: " + ascii(path_b + item_b))
					if (os.path.isdir(path_b+item_b)):
						shutil.rmtree(path_b+item_b)
					else:
						os.remove(path_b + item_b)
			else:	
				print("deleted: " + ascii(path_b + item_b))
				newname_b = "DEL" + today + "__" + item_b
				os.rename(path_b+item_b, path_b+newname_b)



comparecur(root_orig, root_bkup)
