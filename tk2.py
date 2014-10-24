import os
from time import sleep

def redo():
	math()

def math():
	while(1):
		cmd2 = raw_input("Enter Value# ")
		if "ex" in cmd2:
			print("\nQuiting Math Section...\n")
			sleep(2)
			break
		else:
			cmd3 = "echo |awk '{print %s}'" % str(cmd2)
			try:
				cmd = os.system(cmd3)
				print cmd
				redo()
			except OSError as msg:
				print("Error: "), msg[1]
