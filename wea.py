import os
import re
from time import sleep
from urllib2 import urlopen, build_opener

def redo(ips):
	weather(ips)

def check(loc):
	loc = loc
	opener = build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	data = opener.open('http://www.melissadata.com/lookups/iplocation.asp?ipaddress=%s' % loc).read()
	res = re.compile(r'<tr><td class=\'columresult\'>City</td><td align=\'left\'><b>(.*)</b></td></tr>').search(data)
	res2 = re.compile(r'<tr><td class=\'columresult\'>Country<\/td><td align=\'left\'><b>(.*)<\/b><\/td><\/tr>').search(data)
	city = res.group(1)
	country = res2.group(1)
	return(city,country)

def check2(city,country):
	city = city
	country = country
	look = city + " " + country
	opener = build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	data = opener.open('http://www.wunderground.com/cgi-bin/findweather/getForecast?bannertypeclick=htmlSticker&query=%s&GO=GO' % look).read()
	res = re.compile(r'<meta property="og:title" content="(.*) \| (.*)&deg; \| (.*)" \/>').search(data)
	res2 = re.compile(r'<div class="local-time"><i class="fi-clock"><\/i> <span>(.*)<\/span>(.*)<\/div>').search(data)
	res3 = re.compile(r'<span class="wx-value">(.*)<\/span><span class="wx-unit">\%<\/span>').search(data)
	location = res.group(1)
	temp = res.group(2)
	cloud = res.group(3)
	time = res2.group(1)
	gmt = res2.group(2)
	humidity = res3.group(1)
	return(location,temp,cloud,time,gmt,humidity)

def check3(loc):
	look = loc
	opener = build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	data = opener.open('http://www.wunderground.com/cgi-bin/findweather/getForecast?bannertypeclick=htmlSticker&query=%s&GO=GO' % look).read()
	res = re.compile(r'<meta property="og:title" content="(.*) \| (.*)&deg; \| (.*)" \/>').search(data)
	res2 = re.compile(r'<div class="local-time"><i class="fi-clock"><\/i> <span>(.*)<\/span>(.*)<\/div>').search(data)
	res3 = re.compile(r'<span class="wx-value">(.*)<\/span><span class="wx-unit">\%<\/span>').search(data)
	location = res.group(1)
	temp = res.group(2)
	cloud = res.group(3)
	time = res2.group(1)
	gmt = res2.group(2)
	humidity = res3.group(1)
	return(location,temp,cloud,time,gmt,humidity)

def weather(ip):
	ip = ip
	rez = check(ip)
	rez2 = check2(rez[0],rez[1])
	print("\n\tWeather Information: Current Machine Location is %s %s" % (rez[0],rez[1]))
	print("\tInfo: %s is %s and %s degree celcius in Temperature: (Humidity: %s) Time: %s - (%s)" % (rez2[0],rez2[2],rez2[1],rez2[5],rez2[3],rez2[4]))
	print
	sleep(1)
	print("\tTo check other locations, Enter 'State Country'\n")
	while(1):
		cmd = raw_input("Enter Location# ")
		if (len(cmd) < 2):
			print("\nInput Error: Ex: Enter Location# Lagos Nigeria")
			redo(ip)
		else:
			if "ex" in cmd:
				print("\nQuiting Weather Section...\n")
				sleep(1)
				break
				break
			else:
				rez3 = check3(cmd)
				print("\tInfo: %s is %s and %s degree celcius in Temperature: (Humidity: %s) Time: %s - (GMT: %s)" % (rez3[0],rez3[2],rez3[1],rez3[5],rez3[3],rez3[4]))
				redo(ip)
