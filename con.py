import os
import re
from time import sleep
from urllib2 import urlopen, build_opener

def redo():
	convert()

def convert():
	print("\n\t\t\t\t\t\tCurrency Converter - Ex: 500 USD to EUR\n\t\t\t\t\t\t***************************************")
	while(1):
		cmd2 = raw_input("Enter Value# ")
		if (len(cmd2) < 3):
			print("Wrong Convertion Format - Ex: 500 USD to EUR")
			redo()
		elif "exit" in cmd2:
				print("\nQuiting XChange Section...\n")
				sleep(1)
				break
		else:
			try:
				d = re.match(r'(.*) (.*) to (.*)', cmd2, re.M|re.I)
				a = d.group(1)
				b = d.group(2)
				c = d.group(3)
				opener = build_opener()
				opener.addheaders = [('User-agent', 'Mozilla/5.0')]
				data = opener.open('http://www.xe.com/currencyconverter/convert/?Amount=%d&From=%s&To=%s' % (int(a),b,c)).read()
				res = re.compile(r'"rightCol">(\d.*)&nbsp').search(data)
				amount = res.group(1)
				print("XChange: %d From %s To %s = %s" % (int(a),b,c,amount))
				redo()
			except AttributeError:
				print("Error Converting Your Values - Try Again!")
				redo()
