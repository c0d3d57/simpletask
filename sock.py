import sys
import re
import socket
import urllib2 as urllib
from time import sleep

def banner():
	print("\n\tWelcome to the raw socket/http section\n\t*********************************")
	print("\tEnter --socket to check for open port on a host: Enter --http to read any url headers.\n")


def redo():
	check()

def redohttp():
	http()

def urll(url):
	url = "http://www." + url
	url = str(url)
	print("\nFetching Headers for %s" % url)
	conn = urllib.urlopen(url)
	if (conn):
		print("\nPrinting Headers...\n")
		res = conn.info()
		data = conn.read()
		print "URL: ", conn.geturl()
		print "DATE: ", res['date']
		print "SERVER: ", res['server']
		print "TYPE: ", res['content-type']
		print "LENGTH: ", len(data)
		print
		redohttp()
	else:
		print("\nUnable to fetch URL!")

def http():
	print("\n\tThis is the http section of the program\n")
	while(1):
		url = raw_input("Enter URL# ")
		if "exit" in url:
			print("\n\tQuiting http Section...\n")
			sleep(2)
			break
		else:
			print("Testing domain: %s") % url
			url = re.sub(r'http://', "",str(url),1)
			urll(url)

def d_test(host,port):
	host = host
	port = port
	try:
		print("Testing IP Address: "), host
		s = socket.socket(
    		socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
	except socket.error or socket.herror as msg:
		print "Connection Failed: " + str(msg[0]) + " Message " + msg[1]
		sys.exit()
	else:
		print "Connection Success: Port %d is open on %s" % (port, host)
		print
		redo()


def check():
	while 1:
		print("\n\tThis is the raw socket section of the program\n")
		host = raw_input("Enter Host Address: ")
		if "exit" in host:
			print("\n\tQuiting the Socket Section...")
			sleep(2)
			break
		else:
			port = raw_input("Enter Port: ")
			print "You have entered", host, port
			sleep(1)
			print "Now Checking", host, "on port", port
			host = str(host)
			port = int(port)
			p = socket.gethostbyaddr(host)
			print
			print("Host-Name: "), p[0]
			print("IP Address: "), p[2]
			print
			d_test(host, port)
	
def sock():
	banner()
	request = raw_input("Syntax# ")

	if "--check" in request:
		check()
	elif "--http" in request:
		http()
	else:
		banner()
