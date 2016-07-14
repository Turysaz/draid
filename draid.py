#!/usr/bin/python3

# TODO license

infotext = '''This is draid, the "delayed raid" backup software.
Copyright (c) 2016 Turysaz'''

helptext = '''USAGE: draid <command> [<options>] [<parameters>]

commands:
---------
bu			creates backup
	-c		blabla
	-e		blabla

cleanup
	blabla
'''

# start program

import sys

print(infotext)


args = sys.argv[1:]

if len(args)==0:
	print("Error! No command found")
	print(helptext)
	exit()

command = args[0]

if command == "bu":
	print("create backup")
	print("to be added soon")
	
elif command == "mv":
	print("move")
	print("to be added soon")
	
elif command == "rm":
	print("remove")
	print("to be added soon")

elif command == "ls-del":
	print("list deleted files")
	print("to be added soon")

elif command == "find-missing-bu":
	print("find missing backups")
	print("to be added soon")

elif command == "revive":
	print("revive file or directory")
	print("to be added soon")

elif command == "keep":
	print("keep a file in backup for more days")
	print("to be added soon")

elif command == "cleanup":
	print("cleaning up")
	print("to be added soon")

elif command == "help":
	print(helptext)

else:
	print("unknown command: " + command )
	print(helptext)
	
