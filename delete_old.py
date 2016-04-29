import os, shutil

def search_recursively(folder):
	list = os.listdir(folder)
	for file in list:
		deleted = False
		if (file[:3] == "DEL"): 
			a = input("remove " + folder + file + " ? (Y/N)").upper()
			while(a != "Y" and a != "N"):
				a = input("type Y or N!").upper()
			if(a == "Y"):
				print(folder + file + " deleted.")
				if (os.path.isdir(folder + file)):
					shutil.rmtree(folder+file)
				else:
					os.remove(folder+file)
				deleted = True
			else:
				print("keeping " + folder + file)
		if(os.path.isdir(folder+file) and not deleted): 
			search_recursively(folder + file + "/")
			


maindir = "/drives/"

if(maindir[-1] != "/"):
	maindir += "/"

search_recursively(maindir)
