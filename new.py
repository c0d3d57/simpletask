import os
import re
import sys
import math
from urllib import urlopen

print("\n\tFetching System Information...\n\t******************************")
data = str(urlopen('http://checkip.dyndns.com/').read())
MY_IP = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)

pid = os.getcwd()
os = os.uname()

try:
	print
	print("\tMachine Type/Kernel Name:"), os[0]
	print("\tComputer Name: "), os[1]
	print("\tKernel version number: "), os[2]
	print("\tOS Description: "), os[3]
	print("\tMachine hardware name: "), os[4]
	print("\tCurrent working directory: "), pid
	print("\tRemote IP Address: "), MY_IP
except OSError as msg:
	print("\nUnable to collect your machine information: "), msg

print
print("\t***************************************************************************************************************************")

def help():
	print("\n\tTo trigger any of this program's functions, enter the following commands at the command line 'Enter Command >'")
	print("\tEnter 'con' To use the Currency Xchanger\n\tEnter 'math' To use the calculator\n\tEnter 'w' To use the Weather Function\n\tEnter 's' For Socket Function\n")

def banner():
	print("""
		\tHello, I am a basic python program that performs a couple of tasks.
			Such as weather reading, basic math, currency converter and web headers reading.
			To take advantage of either functions, simply enter a command on this same prompt window, ie 'math'\n""")

banner()

from tk2 import *
from con import *
from wea import *
from sock import *

while 1:
	cmd = raw_input("Enter Command > ")
	if "exit" in cmd or "quit" in cmd:
		print("\n\tThank you for trying me out...\n\tGood Bye!\n")
		sys.exit()
	elif "math" in cmd:
		math()
	elif "con" in cmd:
		convert()
	elif "w" in cmd:
		weather(MY_IP)
	elif "h" in cmd:
		help()
	elif "s" in cmd:
		sock()
	else:
		help()
